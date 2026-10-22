import io
import csv
import tempfile
import unittest
import zipfile
from pathlib import Path
from fda_iid import parse_iid, save_iid, load_iid, filter_iid

# Synthetic parser fixtures only; never loaded into the application database.
FIXTURE = b'INGREDIENT_NAME~ROUTE~DOSAGE_FORM~CAS_NUMBER~UNII~POTENCY_AMOUNT~POTENCYUNIT\nPOLYSORBATE 80~INTRAVENOUS~INJECTION~9005-65-6~TEST~0.1~%\nPOLYSORBATE 80~ORAL~SOLUTION~9005-65-6~TEST~1~MG\n'

class IidTests(unittest.TestCase):
    def test_route_preservation_and_alias_search(self):
        snapshot = parse_iid(FIXTURE, 'fixture.txt', 'test version')
        self.assertEqual(len(snapshot['records']), 2)
        matches = filter_iid(snapshot['records'], 'PS80', 'INTRAVENOUS')
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]['potency_unit'], '%')
        self.assertEqual(len(snapshot['metadata']['sha256']), 64)

    def test_zip_without_extraction_and_roundtrip(self):
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as archive:
            archive.writestr('../../fixture.txt', FIXTURE)
        snapshot = parse_iid(buffer.getvalue(), 'fixture.zip', 'test version')
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
            path = Path(folder) / 'iid.json'
            save_iid(snapshot, path)
            self.assertEqual(load_iid(path), snapshot)

    def test_invalid_import_does_not_replace_snapshot(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
            path = Path(folder) / 'iid.json'
            snapshot = parse_iid(FIXTURE, 'fixture.txt', 'test version')
            save_iid(snapshot, path)
            for payload, version in [(b'<html>error</html>', 'test'), (FIXTURE, '')]:
                with self.assertRaises(ValueError):
                    parse_iid(payload, 'bad.txt', version)
            self.assertEqual(load_iid(path), snapshot)

    def test_extra_columns_preserved(self):
        payload = FIXTURE.replace(b'POTENCYUNIT\n', b'POTENCYUNIT~EXTRA\n').replace(b'~%\n', b'~%~X\n').replace(b'~MG\n', b'~MG~Y\n')
        snapshot = parse_iid(payload, 'fixture.txt', 'test')
        self.assertEqual(snapshot['records'][0]['additional_fields'], {'EXTRA': 'X'})

    def test_official_current_zip_and_real_records(self):
        import hashlib
        from fda_iid import DATA, export_iid
        archive = DATA.parent / "fda_iid_2026_10.zip"
        if not archive.exists():
            self.skipTest("Official archive not bundled")
        payload = archive.read_bytes()
        snapshot = parse_iid(payload, archive.name, "2026-10")
        self.assertEqual(snapshot["metadata"]["data_member"], "IIR_OCOMM.xlsx")
        self.assertEqual(snapshot["metadata"]["rows"], 9076)
        self.assertEqual(snapshot["metadata"]["ingredients"], 1795)
        self.assertEqual(snapshot["metadata"]["sha256"], hashlib.sha256(payload).hexdigest())
        cas = filter_iid(snapshot["records"], "9005-65-6")
        ps80 = filter_iid(snapshot["records"], "PS80")
        self.assertEqual(len(cas), 78)
        self.assertEqual(cas, ps80)
        intravenous = filter_iid(ps80, route="INTRAVENOUS")
        self.assertTrue(intravenous)
        exported = list(csv.DictReader(io.StringIO(export_iid(intravenous, snapshot["metadata"]).decode("utf-8-sig"))))
        self.assertEqual(len(exported), len(intravenous))
        self.assertEqual(exported[0]["potency_unit"], intravenous[0]["potency_unit"])
        self.assertIn("maximum_daily_exposure", exported[0])
