"""Curated, public-source CTD mapping data for the CTD Navigator MVP.

The records are intentionally synthetic and contain no sponsor or CDMO data.
"""

SOURCES = {
    "FDA_QUALITY_AGREEMENTS": {"label": "FDA：委托生产质量协议（2016）", "url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/contract-manufacturing-arrangements-drugs-quality-agreements-guidance-industry"},
    "FDA_DATA_INTEGRITY": {"label": "FDA：Data Integrity and Compliance With Drug CGMP（2018）", "url": "https://www.fda.gov/media/119267/download"},
    "FDA_NITROSAMINES": {"label": "FDA：Control of Nitrosamine Impurities in Human Drugs（适用范围需确认）", "url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/control-nitrosamine-impurities-human-drugs"},
    "ICH_Q3C_Q3D_INDEX": {"label": "EMA：杂质指南索引（含 Q3C 残留溶剂 / Q3D 元素杂质）", "url": "https://www.ema.europa.eu/en/human-regulatory-overview/research-development/scientific-guidelines/quality-guidelines/quality-guidelines-impurities"},
    "FDA_PS_RESEARCH": {"label": "FDA Science Forum 2023：聚山梨酯降解研究（研究摘要，非指南）", "url": "https://www.fda.gov/science-research/fda-science-forum/polysorbate-20-degradation-biotherapeutic-formulations-and-its-impact-protein-quality"},
    "ICH_M4Q": {
        "label": "ICH M4Q(R1)：CTD 质量模块结构",
        "url": "https://www.ich.org/page/ctd",
    },
    "FDA_M4Q": {
        "label": "FDA M4Q：The CTD — Quality",
        "url": "https://www.fda.gov/media/71581/download",
    },
    "FDA_IND_CMC": {
        "label": "FDA：IND 申请的 CMC 信息",
        "url": "https://www.fda.gov/drugs/investigational-new-drug-application-ind/ind-applications-clinical-investigations-chemistry-manufacturing-and-control-cmc-information",
    },
    "FDA_CCI": {
        "label": "FDA：稳定性方案中的容器密闭完整性测试",
        "url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/container-and-closure-system-integrity-testing-lieu-sterility-testing-component-stability-protocol",
    },
    "FDA_PV": {
        "label": "FDA：Process Validation — General Principles and Practices",
        "url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/process-validation-general-principles-and-practices",
    },
    "ICH_Q5C": {
        "label": "ICH Q5C：生物技术/生物制品稳定性",
        "url": "https://database.ich.org/sites/default/files/Q5C%20Guideline.pdf",
    },
    "ICH_Q6B": {
        "label": "ICH Q6B：生物技术/生物制品质量标准",
        "url": "https://database.ich.org/sites/default/files/Q6B%20Guideline.pdf",
    },
    "ICH_Q5E": {
        "label": "ICH Q5E：生物制品工艺变更可比性",
        "url": "https://database.ich.org/sites/default/files/Q5E%20Guideline.pdf",
    },
    "ICH_Q2": {
        "label": "ICH Q2(R2)：分析方法验证",
        "url": "https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf",
    },
    "ICH_Q7": {
        "label": "ICH Q7：原料药 GMP（物料、生产、实验室控制）",
        "url": "https://www.ich.org/page/quality-guidelines",
    },
    "ICH_Q8": {
        "label": "ICH Q8(R2)：Pharmaceutical Development（第一部分 2.1.2、2.2.1）",
        "url": "https://database.ich.org/sites/default/files/Q8_R2_Guideline.pdf",
    },
    "ICH_Q11": {
        "label": "ICH Q11：Drug Substance Development and Manufacture",
        "url": "https://www.ich.org/page/quality-guidelines",
    },
    "FDA_ASEPTIC": {
        "label": "FDA：无菌药品无菌工艺 CGMP 指南",
        "url": "https://www.fda.gov/media/71026/download",
    },
    "FDA_CCS": {
        "label": "FDA：药品和生物制品容器密闭系统",
        "url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/container-closure-systems-packaging-human-drugs-and-biologics",
    },
    "ICH_Q1": {"label": "ICH Q1：稳定性", "url": "https://www.ich.org/page/quality-guidelines"},
    "ICH_Q3": {"label": "ICH Q3：杂质", "url": "https://www.ich.org/page/quality-guidelines"},
    "ICH_Q5A": {"label": "ICH Q5A(R2)：生物制品病毒安全性", "url": "https://database.ich.org/sites/default/files/ICH_Q5A%28R2%29_Guideline_2023_1101.pdf"},
    "ICH_Q5D": {"label": "ICH Q5D：细胞基质", "url": "https://database.ich.org/sites/default/files/Q5D_Guideline.pdf"},
    "ICH_Q9": {"label": "ICH Q9(R1)：质量风险管理", "url": "https://www.ich.org/page/quality-guidelines"},
    "ICH_Q10": {"label": "ICH Q10：药品质量体系（3.2.2 CAPA / 3.2.3 变更管理）", "url": "https://database.ich.org/sites/default/files/Q10_Guideline.pdf"},
    "ICH_Q12": {"label": "ICH Q12：药品生命周期管理", "url": "https://www.ich.org/page/quality-guidelines"},
    "ICH_Q14": {"label": "ICH Q14：分析方法开发", "url": "https://www.ich.org/page/quality-guidelines"},
    "ICH_M4Q_R2_DRAFT": {"label": "ICH M4Q(R2)：Step 3 草案（非实施版本）", "url": "https://www.ich.org/page/ctd"},
}


# One report may legitimately map to several sections. ``priority`` describes the
# normal filing destination, not a universal regulatory rule.
RECORDS = [
    {
        "name": "CoA / Certificate of Analysis",
        "zh": "分析证书（CoA）",
        "aliases": ["coa", "certificate of analysis", "分析证书", "检验报告", "放行证书", "批检验结果"],
        "scope": ["DS", "DP"],
        "summary": "汇总某一批次按既定质量标准执行的检测项目、结果与判定。",
        "mappings": {
            "DS": [
                ("3.2.S.4.4", "Batch Analyses / 批分析", "主要", "呈现代表性 DS 批次结果和批次信息。"),
                ("3.2.S.4.1", "Specification / 质量标准", "交叉", "核对检测项目、方法和接受标准。"),
                ("3.2.S.4.2–4.3", "Analytical Procedures & Validation", "交叉", "方法编号、版本和验证状态应可追溯。"),
            ],
            "DP": [
                ("3.2.P.5.4", "Batch Analyses / 批分析", "主要", "呈现代表性 DP 批次结果和批次信息。"),
                ("3.2.P.5.1", "Specification(s) / 质量标准", "交叉", "核对放行/货架期标准及版本。"),
                ("3.2.P.5.2–5.3", "Analytical Procedures & Validation", "交叉", "方法编号、版本和验证状态应可追溯。"),
            ],
        },
        "review": ["批号、批量、生产日期与批用途是否一致", "结果、单位、接受标准及方法版本是否匹配", "OOS/OOT、偏差或重测是否透明说明", "ADC 常见关键属性（DAR、游离药、聚集体、效价）是否覆盖且可追溯"],
        "sources": ["ICH_M4Q", "ICH_Q6B"],
    },
    {
        "name": "Stability report / stability data",
        "zh": "稳定性报告 / 稳定性数据",
        "aliases": ["stability", "stability report", "stability data", "稳定性", "稳定性报告", "稳定性数据", "加速稳定性"],
        "scope": ["DS", "DP"],
        "summary": "支持复验期或货架期、储存条件以及运输/使用期间的质量保持。",
        "mappings": {
            "DS": [
                ("3.2.S.7.3", "Stability Data / 稳定性数据", "主要", "放置条件、时间点、批次和结果表。"),
                ("3.2.S.7.1", "Stability Summary and Conclusions", "交叉", "趋势评价、复验期及储存条件结论。"),
                ("3.2.S.7.2", "Post-approval Stability Protocol", "交叉", "承诺批及后续稳定性方案。"),
            ],
            "DP": [
                ("3.2.P.8.3", "Stability Data / 稳定性数据", "主要", "放置条件、时间点、批次和结果表。"),
                ("3.2.P.8.1", "Stability Summary and Conclusions", "交叉", "货架期、储存条件及趋势结论。"),
                ("3.2.P.8.2", "Post-approval Stability Protocol", "交叉", "承诺批及后续稳定性方案。"),
            ],
        },
        "review": ["批次是否代表拟上市工艺、容器和规模", "稳定性指示方法及关键降解路径是否充分", "趋势、异常点、缺失时间点和统计外推是否有解释", "ADC 应关注聚集、片段、DAR/载荷分布、游离小分子和效价变化"],
        "sources": ["ICH_M4Q", "ICH_Q5C"],
    },
    {
        "name": "CCI / Container Closure Integrity",
        "zh": "容器密闭完整性（CCI）",
        "aliases": ["cci", "container closure integrity", "ccit", "密闭完整性", "容器密闭", "包装完整性"],
        "scope": ["DP"],
        "summary": "证明容器密闭系统在生产、运输和货架期内维持产品保护与无菌屏障。",
        "mappings": {
            "DP": [
                ("3.2.P.7", "Container Closure System", "主要", "系统构成、材料、规格与适用性总体证据。"),
                ("3.2.P.8.3", "Stability Data", "交叉", "作为稳定性计划一部分时呈现长期/老化后的 CCI 数据。"),
                ("3.2.P.2.4", "Container Closure System Development", "交叉", "方法选择、最差条件和系统设计依据。"),
            ]
        },
        "review": ["确定性方法优先及检测限/泄漏限的科学依据", "阳性对照、系统适用性和方法验证", "最差容器组合、顶空、扭矩/压塞、运输与老化条件", "CCI 结果与无菌保证、稳定性及容器组件变更的衔接"],
        "sources": ["ICH_M4Q", "FDA_CCI"],
    },
    {
        "name": "CIU / Compatibility and In-use study",
        "zh": "配伍性与使用中稳定性（CIU）",
        "aliases": ["ciu", "compatibility and in-use", "in use stability", "in-use", "配伍性", "使用中稳定性", "稀释后稳定性", "给药器具相容性"],
        "scope": ["DP"],
        "summary": "评价复溶、稀释、暂存和给药全过程中产品与接触材料的相容性及质量保持。",
        "mappings": {
            "DP": [
                ("3.2.P.2.6", "Compatibility / 相容性", "主要", "复溶液、稀释液和给药器具相容性。"),
                ("3.2.P.8.3", "Stability Data", "交叉", "使用中时间/温度条件下的结果。"),
                ("3.2.P.1", "Description and Composition", "交叉", "核对浓度、辅料和复溶/稀释方案。"),
            ]
        },
        "review": ["临床实际稀释液、浓度、容器、管路和过滤器是否覆盖", "最差时间/温度、光照及输注过程是否合理", "低浓度吸附、颗粒、聚集、效价及可见异物风险", "结论是否与药房操作和标签说明一致"],
        "sources": ["ICH_M4Q", "ICH_Q5C"],
    },
    {
        "name": "PPQ / Process Performance Qualification",
        "zh": "工艺性能确认（PPQ）",
        "aliases": ["ppq", "process performance qualification", "process validation", "工艺验证", "工艺性能确认", "验证批"],
        "scope": ["DS", "DP"],
        "summary": "以商业化代表性规模证明既定工艺和控制策略能够持续产出合格产品。",
        "mappings": {
            "DS": [
                ("3.2.S.2.5", "Process Validation and/or Evaluation", "主要", "DS 工艺验证策略、方案和结果。"),
                ("3.2.S.2.4", "Controls of Critical Steps and Intermediates", "交叉", "关键步骤、IPC 和中间体标准。"),
                ("3.2.S.4.4", "Batch Analyses", "交叉", "PPQ 批次放行/表征结果。"),
            ],
            "DP": [
                ("3.2.P.3.5", "Process Validation and/or Evaluation", "主要", "DP 工艺验证策略、方案和结果。"),
                ("3.2.P.3.4", "Controls of Critical Steps and Intermediates", "交叉", "关键步骤、IPC 和中间体标准。"),
                ("3.2.P.5.4", "Batch Analyses", "交叉", "PPQ 批次放行/表征结果。"),
            ],
        },
        "review": ["批次数量与选择是否有基于风险和工艺知识的理由", "规模、场地、设备、原料及参数是否具商业代表性", "CPP/CQA、采样点、统计方法和接受标准是否预先定义", "偏差、趋势及持续工艺确认计划是否闭环"],
        "sources": ["ICH_M4Q", "FDA_PV"],
    },
    {
        "name": "Analytical method validation report",
        "zh": "分析方法验证报告",
        "aliases": ["method validation", "analytical validation", "amv", "方法验证", "分析方法验证", "方法确认"],
        "scope": ["DS", "DP"],
        "summary": "证明分析方法适合其预定用途，并支持质量标准与稳定性结论。",
        "mappings": {
            "DS": [("3.2.S.4.3", "Validation of Analytical Procedures", "主要", "DS 方法验证/确认资料。"), ("3.2.S.4.2", "Analytical Procedures", "交叉", "方法描述及版本。")],
            "DP": [("3.2.P.5.3", "Validation of Analytical Procedures", "主要", "DP 方法验证/确认资料。"), ("3.2.P.5.2", "Analytical Procedures", "交叉", "方法描述及版本。")],
        },
        "review": ["预定用途与验证特性、范围和接受标准是否一致", "特异性、准确度、精密度、线性/范围及稳健性", "关键试剂、系统适用性和数据处理规则", "IND 阶段适用性与 BLA 阶段完整验证的差距是否明确"],
        "sources": ["ICH_M4Q", "ICH_Q2"],
    },
    {
        "name": "Comparability study",
        "zh": "可比性研究",
        "aliases": ["comparability", "comparability study", "可比性", "工艺变更可比性", "pre post change"],
        "scope": ["DS", "DP"],
        "summary": "评估工艺、场地、规模或分析方法变更前后产品的质量可比性。",
        "mappings": {
            "DS": [("3.2.S.2.6", "Manufacturing Process Development", "主要", "DS 工艺演变和变更可比性。"), ("3.2.S.3.1–3.2", "Characterisation", "交叉", "结构、活性与杂质对比。")],
            "DP": [("3.2.P.2.3", "Manufacturing Process Development", "主要", "DP 工艺演变和变更可比性。"), ("3.2.P.5.4–5.6", "Control of Drug Product", "交叉", "批数据、杂质和结论支持。")],
        },
        "review": ["变更描述、风险评估和可比性问题陈述是否清楚", "批次、方法和属性是否有足够区分力", "关键质量属性差异是否有临床/非临床桥接意义", "结论、剩余不确定性和后续承诺是否匹配"],
        "sources": ["ICH_M4Q", "ICH_Q5E"],
    },
    {
        "name": "Process characterization report",
        "zh": "工艺表征报告",
        "aliases": ["process characterization", "process characterization report", "pcr", "工艺表征", "参数表征", "design space"],
        "scope": ["DS", "DP"],
        "summary": "识别工艺参数、物料属性与 CQA 的关系，形成参数范围和控制策略。",
        "mappings": {
            "DS": [("3.2.S.2.6", "Manufacturing Process Development", "主要", "DS 工艺知识和参数研究。"), ("3.2.S.2.4", "Controls of Critical Steps", "交叉", "研究结论转化为工艺控制。")],
            "DP": [("3.2.P.2.3", "Manufacturing Process Development", "主要", "DP 工艺知识和参数研究。"), ("3.2.P.3.4", "Controls of Critical Steps", "交叉", "研究结论转化为工艺控制。")],
        },
        "review": ["风险评估与研究范围是否相互印证", "缩小模型/DoE 与商业工艺的代表性", "参数交互、边缘条件和统计模型充分性", "结论是否真正落实到 CPP、范围和监测策略"],
        "sources": ["ICH_M4Q", "FDA_PV"],
    },
    {
        "name": "Viral clearance validation report",
        "zh": "病毒清除验证报告",
        "aliases": ["viral clearance", "virus clearance", "病毒清除", "病毒灭活", "病毒验证"],
        "scope": ["DS"],
        "summary": "证明生产工艺中的正交步骤具有清除/灭活潜在病毒污染的能力。",
        "mappings": {
            "DS": [("3.2.S.2.5", "Process Validation and/or Evaluation", "主要", "生物制品 DS 病毒清除研究。"), ("3.2.S.2.4", "Controls of Critical Steps", "交叉", "病毒清除关键参数与步骤控制。")]
        },
        "review": ["模型病毒选择及与潜在风险的相关性", "缩小模型、最差条件和步骤独立性", "清除因子计算、检测方法和细胞毒/干扰控制", "累计清除能力与原料/细胞基质病毒安全策略"],
        "sources": ["ICH_M4Q"],
    },
    {
        "name": "Cell bank characterization report",
        "zh": "细胞库表征报告",
        "aliases": ["cell bank", "mcb", "wcb", "cell bank characterization", "细胞库", "主细胞库", "工作细胞库", "细胞基质"],
        "scope": ["DS"],
        "summary": "描述生产细胞基质的来源、建立、表征与安全性控制。",
        "mappings": {
            "DS": [("3.2.S.2.3", "Control of Materials", "主要", "细胞库系统、来源和检测。"), ("3.2.S.2.6", "Manufacturing Process Development", "交叉", "细胞基质/库系统演变与变更。")]
        },
        "review": ["来源、构建历史、代次和库层级是否清晰", "身份、纯度、遗传稳定性和外源因子检测", "检测方法覆盖范围及样品代表性", "ADC 抗体生产细胞库与工艺版本是否一致"],
        "sources": ["ICH_M4Q"],
    },
    {
        "name": "Reference standard qualification",
        "zh": "对照品定值/确认报告",
        "aliases": ["reference standard", "reference material", "对照品", "标准品", "参考品", "对照品定值"],
        "scope": ["DS", "DP"],
        "summary": "建立工作/一级对照品的身份、效价、纯度、赋值和生命周期管理。",
        "mappings": {
            "DS": [("3.2.S.5", "Reference Standards or Materials", "主要", "DS 对照品来源、制备、表征和控制。")],
            "DP": [("3.2.P.6", "Reference Standards or Materials", "主要", "DP 专用对照品；常交叉引用 DS 对照品章节。")],
        },
        "review": ["一级与工作对照品的溯源关系", "定值方案、正交表征和不确定度", "稳定性、储存、复测和更换/桥接策略", "不同方法是否使用合适的专属性参考材料"],
        "sources": ["ICH_M4Q", "ICH_Q6B"],
    },
    {
        "name": "Extractables and leachables report",
        "zh": "可提取物与浸出物（E&L）报告",
        "aliases": ["extractables", "leachables", "e&l", "el study", "可提取物", "浸出物", "包材相容性"],
        "scope": ["DP"],
        "summary": "评价容器、密闭件和给药接触材料向产品迁移物质的质量与安全风险。",
        "mappings": {
            "DP": [("3.2.P.2.4", "Container Closure System Development", "主要", "材料选择和相容性风险研究。"), ("3.2.P.7", "Container Closure System", "交叉", "组件、材料和供应商规格。"), ("3.2.P.8.3", "Stability Data", "交叉", "实际浸出物随时间变化的数据。")]
        },
        "review": ["接触材料、提取条件和最差场景覆盖", "分析评价阈值、鉴定能力与未知峰处理", "毒理学评估和每日暴露量假设", "实际浸出物数据与货架期、给药方式的关联"],
        "sources": ["ICH_M4Q"],
    },
]

# A broader operational catalogue is kept separately so this core file remains
# readable. All entries use the same schema and public-source identifiers.
from extra_data import EXTRA_RECORDS  # noqa: E402
from pro_terms import TERM_RECORDS  # noqa: E402

RECORDS.extend(EXTRA_RECORDS)
RECORDS.extend(TERM_RECORDS)

_CORE_CATEGORIES = {
    "CoA / Certificate of Analysis": "放行与批记录",
    "Stability report / stability data": "稳定性与运输",
    "CCI / Container Closure Integrity": "包材与密闭系统",
    "CIU / Compatibility and In-use study": "制剂开发与使用",
    "PPQ / Process Performance Qualification": "工艺与验证",
    "Analytical method validation report": "分析方法与质量标准",
    "Comparability study": "变更与可比性",
    "Process characterization report": "工艺与验证",
    "Viral clearance validation report": "生物安全",
    "Cell bank characterization report": "细胞库与生物安全",
    "Reference standard qualification": "分析方法与质量标准",
    "Extractables and leachables report": "包材与密闭系统",
}
_REVIEW_EN = {
    "原辅料与供应商": ["Confirm material identity, grade, supplier and traceability.", "Verify approved specifications, methods and sampling strategy.", "Assess source, microbiological and impurity risks.", "Confirm change notification and lifecycle controls."],
    "放行与批记录": ["Confirm batch identity, intended use and manufacturing version.", "Reconcile manufacturing, IPC, deviation and test records.", "Verify specifications, method versions and disposition rationale.", "Trace the batch consistently across stability and submission tables."],
    "包材与密闭系统": ["Confirm component identity, material, drawing and supplier.", "Assess protection, compatibility, integrity and functionality.", "Review sterilization, depyrogenation and incoming controls where applicable.", "Link changes to CCI, E&L and stability risks."],
    "工艺与验证": ["Confirm protocol scope and predefined acceptance criteria.", "Assess scale, equipment, batches and worst-case representativeness.", "Review deviations, statistics and linkage to CPPs/CQAs.", "Confirm conclusions and continued verification commitments."],
    "无菌与微生物控制": ["Confirm the contamination-control strategy and process boundary.", "Assess worst-case interventions, loads, durations and operators.", "Verify microbiological methods, controls and acceptance criteria.", "Review failures, investigations and requalification triggers."],
    "设施设备与清洁": ["Confirm intended use, system boundary and qualification status.", "Assess worst-case equipment, locations, loads and operating ranges.", "Verify calibration, maintenance, sampling and analytical controls.", "Review deviations, trends and periodic requalification."],
    "分析方法与质量标准": ["Define intended use and scientifically justified acceptance criteria.", "Assess method principle, critical reagents and system suitability.", "Verify validation characteristics, range and sample stability.", "Confirm lifecycle status, version and transfer readiness."],
    "身份与结构 / Identity & Structure": ["Confirm the structural attribute and intended conclusion.", "Use orthogonal methods where scientifically appropriate.", "Assess method resolution, controls and reference materials.", "Link results to identity, function and batch consistency."],
    "纯度与异质性 / Purity & Heterogeneity": ["Define the variant or impurity population being measured.", "Assess separation, detection and quantitation capability.", "Review orthogonal evidence and peak assignment.", "Link trends and limits to process capability and stability."],
    "效价与生物学活性 / Potency & Bioactivity": ["Demonstrate relevance to the mechanism of action.", "Assess reference standard, curve model and system suitability.", "Verify precision, range, parallelism and robustness.", "Link potency to characterization, release and stability."],
    "ADC 专属性检测 / ADC-specific Tests": ["Define the ADC-specific attribute and molecular population.", "Assess orthogonality, sample preparation and method bias.", "Verify sensitivity to conjugation and degradation changes.", "Link the result to potency, safety, PK and stability."],
    "常规理化检测 / General Physicochemical Tests": ["Confirm compendial or product-specific method status.", "Assess sample handling, instrument suitability and units.", "Verify limits against development, batch and stability data.", "Check consistency between release and shelf-life controls."],
    "微生物与安全性检测 / Microbiology & Safety": ["Define the safety risk and required detection capability.", "Assess sampling, method suitability and interference controls.", "Verify controls, limits and relevant compendial expectations.", "Link excursions to batch impact and contamination control."],
    "稳定性与运输": ["Confirm representative batches, containers and conditions.", "Assess stability-indicating methods and protocol coverage.", "Review trends, excursions and statistical treatment.", "Verify shelf life, handling and transport conclusions."],
    "表征与杂质": ["Define the attribute or impurity and its origin.", "Assess orthogonal characterization and quantitative capability.", "Evaluate process clearance, safety and clinical relevance.", "Link conclusions to specifications and control strategy."],
    "质量体系与变更": ["Define scope, chronology and impacted products or batches.", "Assess risk, root cause and affected submission commitments.", "Verify CAPA, comparability and implementation evidence.", "Confirm regulatory reporting and effectiveness checks."],
    "开发与控制策略 / Development & Control Strategy": ["Use a clear, project-consistent definition.", "Link the concept to product and process understanding.", "Show how risks are translated into controls.", "Maintain traceability through lifecycle changes."],
    "分析生命周期 / Analytical Lifecycle": ["Define the analytical procedure's intended purpose.", "Link performance criteria to development and validation.", "Control critical parameters, reagents and system suitability.", "Manage transfer, changes and ongoing monitoring."],
    "知识与风险管理 / Knowledge & Risk": ["Document the source and relevance of knowledge.", "State assumptions, uncertainty and product-specific gaps.", "Use the evidence transparently in risk decisions.", "Update conclusions as product knowledge evolves."],
    "生命周期管理 / Lifecycle Management": ["Define the regulatory scope and approved baseline.", "Identify conditions, studies and reporting categories.", "Maintain traceability of implementation and commitments.", "Assess cumulative impact across markets and lifecycle."],
    "稳定性设计 / Stability Design": ["Justify the reduced design scientifically.", "Define factors, levels, batches and time points.", "State assumptions required for inference.", "Predefine actions if trends or failures invalidate the design."],
    "工艺中控检测 / In-process Tests": ["Define the process decision supported by the test.", "Confirm sampling point, frequency, speed and method range.", "Establish alert/action limits and adjustment rules.", "Link the result to CPPs, CQAs, yield and batch disposition."],
    "包材与功能性检测 / Packaging & Functionality": ["Link the method to the relevant defect or functional requirement.", "Verify positive controls, detection capability and system suitability.", "Cover worst-case components, assembly, transport and aging.", "Connect results to CCI, sterility assurance and change control."],
    "配方与工艺残留 / Formulation & Process Residues": ["Define the source and quality risk of the analyte.", "Confirm method sensitivity, specificity and sample handling.", "Justify limits using process capability, safety and stability data.", "Trend results across batches and lifecycle changes."],
}
for _record in RECORDS:
    _record.setdefault("category", _CORE_CATEGORIES.get(_record["name"], "其他"))
    _record.setdefault("filing_note", "通常以总结、表格或报告形式支持相应 CTD 章节；具体粒度取决于申报策略。")
    _record.setdefault("term_type", "报告/研究 / Report or Study")
    _record.setdefault("review_en", _REVIEW_EN.get(_record["category"], [
        "Confirm scope, intended use and document status.",
        "Verify scientific rationale, controls and acceptance criteria.",
        "Review data integrity, traceability and deviations.",
        "Confirm conclusions, cross-references and lifecycle impact.",
    ]))


CONTEXT_GUIDANCE = {
    "IND": {
        "label": "IND（临床开发）",
        "headline": "阶段适宜、聚焦受试者安全与临床批可追溯性",
        "notes": [
            "信息深度应随临床阶段、暴露时间和风险递增；不是所有 BLA 成熟度证据都需在早期一次提交。",
            "优先确认身份、质量、纯度、强度/效价、无菌保证及临床批和拟用批之间的关联。",
            "清楚列出暂缺数据、临时标准、计划完成时间和后续承诺。",
        ],
        "source": "FDA_IND_CMC",
    },
    "BLA": {
        "label": "BLA（上市许可）",
        "headline": "商业化代表性、验证完成度与全生命周期控制",
        "notes": [
            "期望商业工艺、场地、规模、控制策略和分析方法形成完整且相互一致的证据链。",
            "重点检查 PPQ、方法验证、长期稳定性、设施/设备以及持续确认计划的成熟度。",
            "模块内和模块间的批号、版本、标准、承诺与交叉引用应可审计且一致。",
        ],
        "source": "FDA_PV",
    },
}


from evidence_data import batch_records, enrich_records

RECORDS.extend(batch_records())
enrich_records(RECORDS)

from original_profiles import upgrade_original_records
upgrade_original_records(RECORDS)

from scenario_data import scenario_records
RECORDS.extend(scenario_records())
