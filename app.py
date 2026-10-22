"""CTD Navigator Pro — bilingual M4Q productivity workspace."""

import csv
import io
import os
import zipfile

import streamlit as st

from ctd_data import CONTEXT_GUIDANCE, RECORDS, SOURCES
from ctd_sections import CTD_SECTIONS
from navigator import confidence_label, normalize, search_records
from fda_iid import SOURCE as IID_SOURCE, parse_iid, save_iid, load_iid, filter_iid, export_iid

st.set_page_config(page_title="CTD Navigator Pro", page_icon="🧭", layout="wide")
st.markdown("""
<style>
.stApp{background:#f5f7fa}.block-container{max-width:1280px;padding-top:1.6rem}
.hero{padding:1.45rem 1.7rem;border-radius:18px;color:white;background:linear-gradient(120deg,#132f4c,#116073 58%,#178276);box-shadow:0 10px 28px #17324f25;margin-bottom:1rem}
.hero h1{margin:0 0 .25rem;font-size:2rem}.hero p{margin:0;color:#dcecf0}.eyebrow{font-size:.74rem;letter-spacing:.13em;text-transform:uppercase;opacity:.82}
.result-card{background:white;border:1px solid #dfe6ed;border-radius:13px;padding:1rem 1.1rem;margin:.55rem 0}
.ctd-code{display:inline-block;color:#07596a;background:#e4f3f2;border-radius:999px;padding:.2rem .62rem;font-weight:700;margin-right:.35rem}
.priority{color:#7a5200;background:#fff1c6;border-radius:999px;padding:.14rem .48rem;font-size:.77rem}.muted{color:#617181;font-size:.88rem}
.notice{border-left:4px solid #d8931a;background:#fff8e8;padding:.7rem 1rem;border-radius:8px;margin:.5rem 0 1rem}
div[data-testid="stMetric"]{background:white;border:1px solid #e1e7ed;padding:.75rem;border-radius:12px}
</style>""", unsafe_allow_html=True)
st.markdown("""<div class="hero"><div class="eyebrow">ADC / CDMO · CMC Regulatory Affairs</div>
<h1>CTD Navigator Pro</h1><p>M4Q 双语章节地图 · 检测与术语库 · 工艺开发与 QA 场景 · 项目清单</p></div>""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("项目语境 / Context")
    scope = st.radio("对象 / Product level", ["DS", "DP"], horizontal=True)
    submission = st.radio("阶段 / Stage", ["IND", "BLA"], horizontal=True)
    st.divider()
    st.markdown("**法规基线 / Regulatory baseline**")
    st.success("M4Q(R1) · 当前实施结构")
    st.warning("M4Q(R2) · Step 3 草案，仅作前瞻参考")
    st.caption("R2 草案目前不用于替换本工具中的现行归档编号。")
    st.divider()
    st.caption("数据边界 / Data boundary")
    st.write("公开 ICH/FDA 来源 · 本地术语与 IID 数据")

ctx = CONTEXT_GUIDANCE[submission]
scope_records = [r for r in RECORDS if scope in r["scope"]]
term_types = sorted({r["term_type"] for r in scope_records})
categories = sorted({r["category"] for r in scope_records})
m1, m2, m3, m4 = st.columns(4)
m1.metric("当前视图 / View", f"{scope} · {submission}")
m2.metric("条目 / Entries", len(scope_records))
m3.metric("检测项目 / Tests", sum(r["term_type"].startswith("检测") for r in scope_records))
m4.metric("M4Q 章节 / Sections", sum((scope == "DS" and ".S" in s["code"]) or (scope == "DP" and ".P" in s["code"]) for s in CTD_SECTIONS))
st.markdown('<div class="notice"><b>辅助建议 / Decision support only.</b> 实际归档取决于产品、地区、申报策略和文件内容；请由项目 RA/CMC 专家确认。M4Q(R2) 截至当前仍为草案。</div>', unsafe_allow_html=True)

search_tab, map_tab, library_tab, checklist_tab, source_tab, iid_tab = st.tabs([
    "🔎 智能检索 / Search", "🗺️ M4Q 章节地图 / Map", "📚 检测与术语库 / Library",
    "✅ 项目清单 / Checklist", "🔗 指南矩阵 / Sources", "FDA 辅料库 / IID"
])

with search_tab:
    left, right = st.columns([2.4, 1])
    with left:
        query = st.text_input("输入报告、检测、缩写或术语 / Report, test, acronym or term", placeholder="例如：SEC、PS80、工艺放大、参数超限、CAPA、质量协议…")
    with right:
        st.markdown(f"**{ctx['label']}**")
        st.caption(ctx["headline"])
        st.caption("阶段切换改变证据重点；CTD 章节按资料用途确定。IND 还需结合具体临床阶段。")
    examples = ["SEC", "HCP", "PS80", "工艺放大", "技术转移", "CAPA", "数据完整性"]
    cols = st.columns(len(examples))
    for col, example in zip(cols, examples):
        if col.button(example, use_container_width=True):
            query = example
    if query:
        results = search_records(query, scope)
        st.markdown(f"#### 结果 / Results · {len(results)}")
        if not results:
            st.warning("未找到匹配项 / No close match. Try a full name, acronym, or browse the library.")
        for index, (score, record) in enumerate(results):
            title = f"{record['zh']} · {record['name']}"
            with st.expander(f"{index + 1}. {title}　｜　{confidence_label(score)} {score:.0%}", expanded=index == 0):
                st.caption(f"{record['term_type']}　·　{record['category']}")
                st.write(record["summary"])
                if record.get("basics"):
                    st.markdown("##### 基础认识 · 是什么与应用场景")
                    for heading, explanation in record["basics"].items():
                        st.markdown(f"**{heading}**：{explanation}")
                if record.get("stage_guidance"):
                    st.markdown(f"##### {submission} 阶段 · 证据重点")
                    st.caption(record["stage_guidance_level"])
                    for heading, explanation in record["stage_guidance"][submission].items():
                        st.markdown(f"**{heading}**：{explanation}")
                if record.get("work_scenario"):
                    st.markdown("##### 工作中怎么判断")
                    for heading, explanation in record["work_scenario"].items():
                        st.markdown(f"**{heading}**：{explanation}")
                if record.get("ra_insight"):
                    st.markdown("##### RA 证据解读")
                    for heading, explanation in record["ra_insight"].items():
                        if heading in ("IND 阶段", "BLA 阶段"):
                            continue
                        st.markdown(f"**{heading}**：{explanation}")
                st.info(f"**CTD 收载方式 / Filing approach：** {record['filing_note']}")
                st.markdown("##### 建议章节 / Suggested CTD location")
                for code, label, priority, reason in record["mappings"][scope]:
                    st.markdown(f'<div class="result-card"><span class="ctd-code">{code}</span><span class="priority">{priority}</span><br><b>{label}</b><div class="muted" style="margin-top:.35rem">{reason}</div></div>', unsafe_allow_html=True)
                cn, en, refs = st.columns([1, 1, .9])
                with cn:
                    st.markdown("##### 审阅要求 · 中文")
                    for item in record["review"]:
                        st.markdown(f"- {item}")
                with en:
                    st.markdown("##### Review requirements · English")
                    for item in record["review_en"]:
                        st.markdown(f"- {item}")
                with refs:
                    st.markdown("##### 监管依据 / References")
                    for source_id in record["sources"]:
                        item = SOURCES[source_id]
                        st.markdown(f"- [{item['label']}]({item['url']})")
    else:
        st.info("输入任意中英文术语或点击样例。可查报告、检测项目、工艺概念和法规专用名词。")

with map_tab:
    st.markdown("### M4Q(R1) Module 3 双语章节地图")
    st.caption("Operational M4Q(R1) structure. R2 draft is tracked separately and does not replace current filing locations.")
    prefixes = {"DS": "3.2.S", "DP": "3.2.P"}
    include_appendix = st.checkbox("包含附录和地区资料 / Include appendices and regional information", value=True)
    sections = [s for s in CTD_SECTIONS if s["code"].startswith(prefixes[scope]) or (include_appendix and (s["code"].startswith("3.2.A") or s["code"] == "3.2.R"))]
    section_query = st.text_input("筛选章节 / Filter sections", key="section_query", placeholder="例如：stability、稳定性、3.2.P.7")
    if section_query:
        q = normalize(section_query)
        sections = [s for s in sections if q in normalize(" ".join([s["code"], s["en"], s["zh"], s["purpose"], " ".join(s["guides"])]))]
    st.dataframe([{"章节 / Section": s["code"], "English": s["en"], "中文": s["zh"], "用途 / Purpose": s["purpose"], "关联 ICH": ", ".join(s["guides"])} for s in sections], use_container_width=True, hide_index=True, column_config={"用途 / Purpose": st.column_config.TextColumn(width="large")})

with library_tab:
    st.markdown("### 检测、报告与专用术语库 / Test, Report & Terminology Library")
    f1, f2, f3 = st.columns([1, 1, 1.5])
    with f1:
        selected_types = st.multiselect("类型 / Type", term_types, default=term_types)
    with f2:
        selected_categories = st.multiselect("分类 / Category", categories, default=categories)
    with f3:
        lib_query = st.text_input("库内筛选 / Filter library", placeholder="中英文名称、别名或 CTD 编号")
    visible = [r for r in scope_records if r["term_type"] in selected_types and r["category"] in selected_categories]
    if lib_query:
        q = normalize(lib_query)
        visible = [r for r in visible if q in normalize(" ".join([r["name"], r["zh"], " ".join(r["aliases"]), r["category"], " ".join(m[0] for m in r["mappings"][scope])]))]
    rows = [{"类型 / Type": r["term_type"], "分类 / Category": r["category"], "中文": r["zh"], "English": r["name"], "CTD": "；".join(m[0] for m in r["mappings"][scope]), "收载方式 / Filing": r["filing_note"], "阶段": submission, "阶段证据重点": r["stage_guidance"][submission]["重点"], "内容深度": r["stage_guidance_level"]} for r in visible]
    st.caption(f"显示 / Showing：{len(rows)}")
    st.dataframe(rows, use_container_width=True, hide_index=True, column_config={"收载方式 / Filing": st.column_config.TextColumn(width="large")})
    output = io.StringIO()
    if rows:
        export_rows = []
        for row, record in zip(rows, visible):
            export_row = dict(row)
            export_row.update({f"基础认识：{k}": v for k, v in record["basics"].items()})
            export_row.update({f"RA：{k}": v for k, v in record["ra_insight"].items() if k not in ("IND 阶段", "BLA 阶段")})
            export_row.update({f"工作场景：{k}": v for k, v in record.get("work_scenario", {}).items()})
            export_row["IND 证据重点"] = record["stage_guidance"]["IND"]["重点"]
            export_row["BLA 证据重点"] = record["stage_guidance"]["BLA"]["重点"]
            export_row["来源链接"] = "；".join(SOURCES[key]["url"] for key in record["sources"])
            export_rows.append(export_row)
        fields = list(dict.fromkeys(key for row in export_rows for key in row))
        writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(export_rows)
    st.download_button("下载当前库 / Download CSV", output.getvalue().encode("utf-8-sig"), f"ctd_navigator_{scope}_library.csv", "text/csv")

with checklist_tab:
    st.markdown("### 项目资料清单生成器 / Project Evidence Checklist")
    st.caption("选择需要跟踪的报告、检测或术语，填写责任人与状态后导出。清单仅保留在当前访问会话，刷新或服务休眠后可能丢失，请及时导出；不同访问者的清单独立。")
    options = {f"{r['zh']} | {r['name']}": r for r in scope_records}
    selected = st.multiselect("选择条目 / Select entries", list(options), placeholder="可搜索并多选")
    checklist_rows = []
    for label in selected:
        r = options[label]
        checklist_rows.append({"中文": r["zh"], "English": r["name"], "类型 / Type": r["term_type"], "CTD": "；".join(m[0] for m in r["mappings"][scope]), "申报阶段 / Stage": submission, "阶段证据重点": r["stage_guidance"][submission]["重点"], "状态 / Status": "未开始 / Not started", "责任人 / Owner": "", "到期日 / Due": "", "备注 / Notes": ""})
    if checklist_rows:
        edited = st.data_editor(checklist_rows, use_container_width=True, hide_index=True, column_config={"状态 / Status": st.column_config.SelectboxColumn(options=["未开始 / Not started", "进行中 / In progress", "待审阅 / In review", "完成 / Complete", "不适用 / N/A"])})
        checklist_csv = io.StringIO()
        writer = csv.DictWriter(checklist_csv, fieldnames=edited[0].keys(), lineterminator="\n")
        writer.writeheader(); writer.writerows(edited)
        st.download_button("导出项目清单 / Export checklist", checklist_csv.getvalue().encode("utf-8-sig"), f"{scope}_{submission}_ctd_checklist.csv", "text/csv")
    else:
        st.info("先选择一个或多个条目 / Select one or more entries to build a checklist.")

with source_tab:
    st.markdown("### ICH/FDA 指南矩阵 / Guidance Matrix")
    st.warning("M4Q(R2) 当前为 Step 3 草案，并非实施版本；本工具继续使用 M4Q(R1) 章节编号。")
    for source_id, item in SOURCES.items():
        st.markdown(f"- **{source_id}** — [{item['label']}]({item['url']})")

st.divider()
st.caption("CTD Navigator Pro · 教学与申报导航辅助 / Training and dossier-navigation support · 不构成法规或法律意见 / Not regulatory or legal advice")


with iid_tab:
    st.markdown("### FDA 辅料数据库 · 批量导入与检索")
    st.markdown(f"从 [FDA 官方下载页]({IID_SOURCE}) 获取 ZIP、XLSX 或 CSV/TXT 文件后导入。")
    st.caption("IID 提供既往辅料使用记录，不提供检测方法或自动生成的 RA 结论。该库独立于人工维护的术语解释，不受 DS/DP 或 IND/BLA 切换影响。")
    if os.environ.get("CTD_ALLOW_IID_IMPORT", "1") == "1":
        with st.expander("导入或更新 FDA 文件"):
            version = st.text_input("文件发布版本", placeholder="例如 2026-07，以 FDA 下载页和文件信息为准", key="iid_version")
            uploaded = st.file_uploader("FDA IID 下载文件", type=["zip", "xlsx", "csv", "txt"], key="iid_upload")
            if uploaded is not None:
                try:
                    candidate = parse_iid(uploaded.getvalue(), uploaded.name, version)
                    st.write(f"格式校验通过：{candidate['metadata']['rows']} 条记录，{candidate['metadata']['ingredients']} 个辅料名称。")
                    st.dataframe(candidate["records"][:5], hide_index=True, use_container_width=True)
                    st.caption("确认导入会保存到本机项目，替换当前 IID 快照；人工术语库保持独立。文件来源和版本由导入者确认。")
                    if st.button("确认导入该版本", key="iid_import"):
                        save_iid(candidate)
                        st.success("已导入并保存。")
                except (ValueError, OSError, csv.Error, zipfile.BadZipFile, RuntimeError, IndexError) as error:
                    st.error(str(error))
    else:
        st.caption("在线版使用随版本发布的 FDA 数据；数据由维护者统一更新。")
    try:
        snapshot = load_iid()
    except (ValueError, OSError):
        snapshot = None
        st.error("本地 IID 数据无法读取，请重新导入有效文件。")
    if snapshot:
        meta = snapshot["metadata"]
        st.caption(f"当前版本：{meta['version']} · {meta['rows']} 条记录 · {meta['ingredients']} 个辅料名称 · 导入时间（UTC）：{meta['imported_at']}")
        st.caption(meta["provenance"])
        if meta.get("source_url"):
            st.markdown(f"[原始 FDA 下载文件]({meta['source_url']})")
        st.caption("Potency 为原始用量字段；maximum_daily_exposure 为最大每日暴露字段，两者分开保留，空白表示本记录未提供。")
        st.info("FDA 历史使用记录不等于当前产品获批、安全上限或推荐用量。请结合给药途径、剂型、单位及产品自身证据解释 Potency 字段。")
        iid_query = st.text_input("查辅料名称、CAS 或 UNII", placeholder="例如 PS80、POLYSORBATE 80", key="iid_query")
        routes = sorted({r["route"] for r in snapshot["records"]})
        route_choice = st.selectbox("给药途径", ["全部途径"] + routes, key="iid_route")
        route = "" if route_choice == "全部途径" else route_choice
        forms = sorted({r["dosage_form"] for r in snapshot["records"] if not route or r["route"] == route})
        form_choice = st.selectbox("剂型", ["全部剂型"] + forms, key="iid_form")
        form = "" if form_choice == "全部剂型" else form_choice
        matches = filter_iid(snapshot["records"], iid_query, route, form)
        st.caption(f"匹配 {len(matches)} 条，页面最多展示 500 条；CSV 导出全部匹配记录。")
        st.dataframe([{k: v for k, v in r.items() if k != "additional_fields"} for r in matches[:500]], hide_index=True, use_container_width=True)
        if matches:
            st.download_button("导出 IID 查询结果", export_iid(matches, meta), "fda_iid_results.csv", "text/csv")
        if iid_query:
            related = search_records(iid_query, "DP", limit=3)
            related = [(score, r) for score, r in related if score >= 0.58]
            if related:
                st.markdown("**相关 RA 术语解释**：" + "、".join(r["zh"] for score, r in related if score >= 0.58))
                st.caption("在智能检索页切换至 DP，使用相同名称查看人工维护的解释。")
    else:
        st.info("尚未导入真实 IID 数据。请先下载 FDA 官方文件并在上方导入。")
