"""Offline FDA IID import. Imported facts remain separate from curated RA content."""
import csv
import hashlib
import io
import json
import re
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

DATA = Path(__file__).resolve().parent / 'data' / 'fda_iid.json'
SOURCE = 'https://www.fda.gov/drugs/drug-approvals-and-databases/inactive-ingredients-database-download'
ALIASES = {
    'ingredient': ['inactiveingredient', 'ingredient', 'ingredientname'],
    'route': ['route', 'routeofadministration'],
    'dosage_form': ['dosageform'],
    'cas': ['cas', 'casnumber', 'casno'],
    'unii': ['unii'],
    'potency_amount': ['potencyamount', 'maximumpotency', 'maximumpotencyamount'],
    'potency_unit': ['potencyunit', 'potencyunits', 'unit'],
}

def _key(value):
    return re.sub('[^a-z0-9]', '', value.lower())


def xlsx_to_csv(payload):
    """Read tabular OOXML cell values without Excel or additional dependencies."""
    namespace = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(io.BytesIO(payload)) as book:
        if sum(info.file_size for info in book.infolist()) > 40 * 1024 * 1024:
            raise ValueError('Excel 解压内容超过 40 MB。')
        strings = []
        if 'xl/sharedStrings.xml' in book.namelist():
            root = ET.fromstring(book.read('xl/sharedStrings.xml'))
            strings = [''.join(node.itertext()) for node in root.findall('m:si', namespace)]
        tables = []
        for member in book.namelist():
            if not re.fullmatch(r'xl/worksheets/sheet[0-9]+\.xml', member):
                continue
            root = ET.fromstring(book.read(member))
            table = []
            width = 0
            for row in root.findall('m:sheetData/m:row', namespace):
                values = {}
                for cell in row.findall('m:c', namespace):
                    ref = re.match('[A-Z]+', cell.get('r', ''))
                    if not ref:
                        raise ValueError('Excel 单元格缺少列位置。')
                    column = 0
                    for letter in ref.group():
                        column = column * 26 + ord(letter) - 64
                    if column > 100:
                        continue
                    if cell.find('m:f', namespace) is not None:
                        raise ValueError('IID 主数据不应含公式。')
                    value = cell.findtext('m:v', default='', namespaces=namespace)
                    if cell.get('t') == 's':
                        value = strings[int(value)]
                    elif cell.get('t') == 'inlineStr':
                        value = ''.join(cell.find('m:is', namespace).itertext())
                    values[column - 1] = value
                if not any(values.values()):
                    continue
                width = max(width, max(values) + 1)
                table.append(values)
            if table:
                header = _key(' '.join(table[0].values()))
                if all(any(alias in header for alias in aliases) for aliases in ALIASES.values()):
                    output = io.StringIO()
                    writer = csv.writer(output)
                    writer.writerows([[row.get(column, '') for column in range(width)] for row in table])
                    tables.append(output.getvalue().encode('utf-8-sig'))
        if len(tables) != 1:
            raise ValueError('Excel 中未找到唯一 IID 主数据表。')
        return tables[0]


def parse_iid(payload, filename, version):
    if not version.strip():
        raise ValueError('请填写 FDA 文件的发布版本，例如 2026-07；不要把导入日期当作发布版本。')
    if len(payload) > 20 * 1024 * 1024:
        raise ValueError('文件超过 20 MB。')
    original = payload
    if filename.lower().endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            candidates = [i for i in archive.infolist() if i.filename.lower().endswith(('.csv', '.txt')) and not i.is_dir()]
            data_files = []
            for info in candidates:
                if info.file_size > 20 * 1024 * 1024:
                    raise ValueError('解压后的数据文件超过 20 MB。')
                with archive.open(info) as member:
                    header = member.readline(8192).decode('utf-8-sig', errors='replace')
                normalized = _key(header)
                if all(any(alias in normalized for alias in aliases) for aliases in ALIASES.values()):
                    data_files.append(info)
            if not data_files:
                data_files = [i for i in archive.infolist() if i.filename.lower().endswith('.xlsx') and 'change' not in i.filename.lower()]
            if len(data_files) != 1:
                raise ValueError('ZIP 中未找到唯一 IID 主数据。')
            info = data_files[0]
            if info.file_size > 20 * 1024 * 1024:
                raise ValueError('主数据文件超过 20 MB。')
            payload = archive.read(info)
            if info.filename.lower().endswith('.xlsx'):
                payload = xlsx_to_csv(payload)
    elif filename.lower().endswith('.xlsx'):
        payload = xlsx_to_csv(payload)
    for encoding in ('utf-8-sig', 'utf-16', 'cp1252'):
        try:
            content = payload.decode(encoding)
            break
        except UnicodeError:
            pass
    else:
        raise ValueError('无法识别文件编码。')
    try:
        dialect = csv.Sniffer().sniff(content[:16000], delimiters=',\t~|;')
    except csv.Error:
        raise ValueError('无法识别分隔符；请使用 FDA 的分隔文本下载文件。')
    reader = csv.DictReader(io.StringIO(content), dialect=dialect)
    headers = {_key(h): h for h in (reader.fieldnames or [])}
    mapping = {field: next((headers[a] for a in aliases if a in headers), None) for field, aliases in ALIASES.items()}
    missing = [field for field, header in mapping.items() if not header]
    if missing:
        raise ValueError('缺少 IID 字段：' + ', '.join(missing))
    rows, seen = [], set()
    for line, raw in enumerate(reader, 2):
        if None in raw or any(value is None for value in raw.values()):
            raise ValueError('第 %s 行字段数量不一致。' % line)
        row = {field: raw[header].strip() for field, header in mapping.items()}
        if not row['ingredient'] or not row['route'] or not row['dosage_form']:
            raise ValueError('第 %s 行缺少辅料、给药途径或剂型。' % line)
        row['maximum_daily_exposure'] = raw.get(headers.get('maximumdailyexposure', ''), '').strip()
        row['maximum_daily_exposure_unit'] = raw.get(headers.get('maximumdailyexposureunit', ''), '').strip()
        row['record_updated'] = raw.get(headers.get('recordupdated', ''), '').strip()
        row['additional_fields'] = {k: v.strip() for k, v in raw.items() if k not in mapping.values()}
        identity = json.dumps(row, sort_keys=True, ensure_ascii=False)
        if identity not in seen:
            seen.add(identity)
            rows.append(row)
        if len(rows) > 100000:
            raise ValueError('记录数超出导入范围。')
    if not rows:
        raise ValueError('文件没有数据记录。')
    return {'metadata': {'source_page': SOURCE, 'version': version.strip(), 'filename': Path(filename).name,
                         'imported_at': datetime.now(timezone.utc).isoformat(),
                         'sha256': hashlib.sha256(original).hexdigest(), 'rows': len(rows),
                         'ingredients': len({r['ingredient'] for r in rows}),
                         'data_member': info.filename if filename.lower().endswith('.zip') else Path(filename).name,
                         'provenance': '用户提供的 FDA 格式文件；格式校验不等于官方真实性核验'}, 'records': rows}


def save_iid(snapshot, path=DATA):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


def load_iid(path=DATA):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding='utf-8'))


def filter_iid(rows, query='', route='', dosage_form=''):
    aliases = {'ps80': 'polysorbate 80', 'ps20': 'polysorbate 20', '聚山梨酯80': 'polysorbate 80', '聚山梨酯20': 'polysorbate 20'}
    q = query.lower().strip()
    q = aliases.get(q.replace(' ', ''), q)
    def matches(row):
        text_match = q in ' '.join((row['ingredient'], row['cas'], row['unii'])).lower()
        # FDA CSV may store CAS as an unhyphenated numeric string ending in .00.
        cas_query = re.sub('[^0-9]', '', q)
        cas_value = row['cas'].split('.')[0].replace('-', '')
        cas_match = bool(re.fullmatch(r'[0-9-]+', q)) and bool(cas_query) and cas_query == cas_value
        return (not q or text_match or cas_match) and (not route or row['route'] == route) and (not dosage_form or row['dosage_form'] == dosage_form)
    return [row for row in rows if matches(row)]


def export_iid(rows, metadata):
    output = io.StringIO()
    export = [{**{k: v for k, v in row.items() if k != 'additional_fields'},
               'additional_fields': json.dumps(row['additional_fields'], ensure_ascii=False),
               'source_version': metadata['version'], 'source_page': metadata['source_page']} for row in rows]
    if export:
        writer = csv.DictWriter(output, fieldnames=export[0].keys())
        writer.writeheader()
        writer.writerows(export)
    return output.getvalue().encode('utf-8-sig')
