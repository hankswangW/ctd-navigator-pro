"""Bilingual ADC/biologics test and regulatory terminology catalogue."""

from ctd_sections import SECTION_BY_CODE


def _mapping(scope, codes):
    result = {}
    for side in scope:
        rows = []
        for index, code in enumerate(codes[side]):
            section = SECTION_BY_CODE[code]
            rows.append((code, f"{section['en']} / {section['zh']}", "主要" if index == 0 else "交叉", section["purpose"]))
        result[side] = rows
    return result


def _term(en, zh, aliases, scope, category, term_type, codes, purpose, review, sources):
    return {
        "name": en, "zh": zh, "aliases": aliases, "scope": scope,
        "category": category, "term_type": term_type, "summary": purpose,
        "mappings": _mapping(scope, codes), "review": review, "sources": sources,
        "filing_note": "该项目可能出现在质量标准、方法、验证、表征、批分析或稳定性资料中；应按预定用途决定呈现深度。",
    }


DS_ANALYTICAL = ["3.2.S.4.1", "3.2.S.4.2", "3.2.S.4.3"]
DP_ANALYTICAL = ["3.2.P.5.1", "3.2.P.5.2", "3.2.P.5.3"]
BOTH_ANALYTICAL = {"DS": DS_ANALYTICAL, "DP": DP_ANALYTICAL}
BIO_REVIEW = ["预定用途与接受标准是否明确", "方法原理、关键试剂和系统适用性", "特异性、精密度、范围及样品稳定性", "结果与 CQA、批次和生命周期阶段的关联"]


TERM_RECORDS = []


def _add_analytical(rows, category, purpose_template="用于评价{zh}，支持身份、纯度、效价或质量一致性判断。"):
    for en, zh, aliases, scope in rows:
        codes = {side: BOTH_ANALYTICAL[side] for side in scope}
        TERM_RECORDS.append(_term(en, zh, aliases, scope, category, "检测项目 / Test", codes,
                                  purpose_template.format(zh=zh), BIO_REVIEW, ["ICH_M4Q", "ICH_Q2", "ICH_Q14"]))


_add_analytical([
    ("Peptide mapping", "肽图", ["peptide map", "肽图分析"], ["DS"]),
    ("Intact molecular mass", "完整分子量", ["intact mass", "whole mass", "完整质量"], ["DS"]),
    ("Amino acid sequence", "氨基酸序列", ["sequence confirmation", "序列确认"], ["DS"]),
    ("N-/C-terminal sequence", "N/C 端序列", ["terminal sequence", "末端序列"], ["DS"]),
    ("Disulfide bond mapping", "二硫键定位", ["disulfide mapping", "二硫键图谱"], ["DS"]),
    ("Glycan profile", "糖型图谱", ["glycosylation", "n glycan", "糖基化", "n糖"], ["DS"]),
    ("Post-translational modifications", "翻译后修饰", ["ptm", "氧化脱酰胺", "modification profile"], ["DS"]),
    ("Higher-order structure", "高级结构", ["hos", "higher order", "高级结构表征"], ["DS"]),
    ("Circular dichroism", "圆二色谱", ["cd spectrum", "cd光谱", "圆二色"], ["DS"]),
    ("Differential scanning calorimetry", "差示扫描量热", ["dsc", "热稳定性", "tm"], ["DS"]),
    ("UV/visible spectrum", "紫外/可见吸收光谱", ["uv spectrum", "紫外光谱"], ["DS"]),
    ("Immunochemical identity", "免疫化学鉴别", ["immuno identity", "免疫鉴别"], ["DS", "DP"]),
], "身份与结构 / Identity & Structure")

_add_analytical([
    ("Size-exclusion chromatography", "体积排阻色谱", ["sec", "sec-hplc", "size exclusion", "聚集体sec"], ["DS", "DP"]),
    ("Reducing CE-SDS", "还原 CE-SDS", ["r-ce-sds", "还原毛细管电泳"], ["DS", "DP"]),
    ("Non-reducing CE-SDS", "非还原 CE-SDS", ["nr-ce-sds", "非还原毛细管电泳"], ["DS", "DP"]),
    ("SDS-PAGE", "SDS 聚丙烯酰胺凝胶电泳", ["sds page", "凝胶电泳"], ["DS"]),
    ("Capillary isoelectric focusing", "毛细管等电聚焦", ["cief", "icief", "等电聚焦"], ["DS", "DP"]),
    ("Ion-exchange chromatography", "离子交换色谱", ["iex", "cation exchange", "cex", "电荷异质性"], ["DS", "DP"]),
    ("Reversed-phase HPLC", "反相高效液相色谱", ["rp-hplc", "反相液相"], ["DS", "DP"]),
    ("Hydrophobic interaction chromatography", "疏水作用色谱", ["hic", "疏水色谱"], ["DS"]),
    ("Analytical ultracentrifugation", "分析超速离心", ["auc", "超速离心"], ["DS"]),
    ("Multi-angle light scattering", "多角度光散射", ["mals", "sec-mals", "多角度光散射"], ["DS"]),
    ("Aggregates", "聚集体", ["hmw", "high molecular weight", "高分子量物质"], ["DS", "DP"]),
    ("Fragments", "片段/低分子量物质", ["lmw", "low molecular weight", "片段"], ["DS", "DP"]),
    ("Charge variants", "电荷异质体", ["acidic variants", "basic variants", "酸性峰", "碱性峰"], ["DS", "DP"]),
], "纯度与异质性 / Purity & Heterogeneity")

_add_analytical([
    ("Antigen-binding assay", "抗原结合活性", ["antigen binding", "抗原结合"], ["DS", "DP"]),
    ("Binding ELISA", "结合 ELISA", ["elisa binding", "结合酶联"], ["DS", "DP"]),
    ("Surface plasmon resonance", "表面等离子体共振", ["spr", "biacore", "表面等离子"], ["DS"]),
    ("Bio-layer interferometry", "生物膜干涉", ["bli", "octet", "生物层干涉"], ["DS"]),
    ("Cell-based potency assay", "细胞效价测定", ["cell potency", "cell based assay", "细胞活性"], ["DS", "DP"]),
    ("Cytotoxicity assay", "细胞毒性效价测定", ["cell killing", "细胞杀伤", "cytotoxic potency"], ["DS", "DP"]),
    ("Internalization assay", "内吞测定", ["internalisation", "内化", "内吞活性"], ["DS"]),
    ("ADCC assay", "抗体依赖的细胞介导细胞毒作用测定", ["adcc", "抗体依赖细胞毒"], ["DS"]),
    ("CDC assay", "补体依赖细胞毒作用测定", ["cdc", "补体依赖细胞毒"], ["DS"]),
    ("Fc receptor binding", "Fc 受体结合", ["fcr binding", "fc受体"], ["DS"]),
], "效价与生物学活性 / Potency & Bioactivity")

_add_analytical([
    ("Drug-to-antibody ratio", "平均药物抗体比（DAR）", ["dar", "average dar", "平均载药量"], ["DS"]),
    ("Drug-load distribution", "载药分布", ["dar distribution", "drug distribution", "载药量分布"], ["DS"]),
    ("Conjugation site occupancy", "偶联位点占有率", ["site occupancy", "偶联位点"], ["DS"]),
    ("Free payload", "游离小分子毒素", ["free drug", "free toxin", "游离药物", "游离毒素"], ["DS", "DP"]),
    ("Unconjugated antibody", "未偶联抗体", ["naked antibody", "裸抗", "未偶联单抗"], ["DS"]),
    ("Residual linker", "残留连接子", ["free linker", "游离linker", "连接子残留"], ["DS"]),
    ("Residual linker-payload", "残留连接子-毒素", ["linker payload", "linker-payload残留"], ["DS"]),
    ("Payload-related impurities", "毒素相关杂质", ["payload impurities", "小分子毒素杂质"], ["DS", "DP"]),
    ("Deconjugation / payload loss", "脱偶联/载荷脱落", ["deconjugation", "payload loss", "脱偶联"], ["DS", "DP"]),
    ("Total antibody concentration", "总抗体浓度", ["total antibody", "抗体总量"], ["DS", "DP"]),
    ("Conjugatable antibody", "可偶联抗体比例", ["conjugatable antibody", "可偶联位点"], ["DS"]),
    ("ADC hydrophobicity profile", "ADC 疏水性图谱", ["hydrophobicity profile", "疏水性分布"], ["DS"]),
], "ADC 专属性检测 / ADC-specific Tests")

_add_analytical([
    ("Appearance", "外观", ["visual appearance", "外观检查"], ["DS", "DP"]),
    ("Color and clarity", "颜色与澄清度", ["clarity", "颜色澄清度"], ["DS", "DP"]),
    ("pH", "酸碱度（pH）", ["ph test", "酸碱度"], ["DS", "DP"]),
    ("Osmolality", "渗透压摩尔浓度", ["osmolarity", "渗透压"], ["DP"]),
    ("Protein concentration", "蛋白浓度", ["protein content", "uv concentration", "蛋白含量"], ["DS", "DP"]),
    ("Fill volume", "装量", ["fill weight", "灌装量", "装量差异"], ["DP"]),
    ("Extractable volume", "可提取容量", ["deliverable volume", "可抽取体积"], ["DP"]),
    ("Visible particles", "可见异物", ["visible particulate", "可见颗粒"], ["DP"]),
    ("Subvisible particles", "不溶性微粒/亚可见颗粒", ["sub-visible particles", "svp", "亚可见颗粒"], ["DP"]),
    ("Moisture / water content", "水分", ["water content", "karl fischer", "卡尔费休"], ["DS", "DP"]),
    ("Reconstitution time", "复溶时间", ["reconstitution", "复溶性"], ["DP"]),
    ("Turbidity", "浊度", ["opalescence", "乳光", "浊度检测"], ["DS", "DP"]),
], "常规理化检测 / General Physicochemical Tests")

_add_analytical([
    ("Sterility", "无菌检查", ["sterility test", "无菌"], ["DP"]),
    ("Bacterial endotoxins", "细菌内毒素", ["endotoxin", "bet", "内毒素"], ["DS", "DP"]),
    ("Bioburden", "生物负载", ["microbial load", "微生物负载"], ["DS", "DP"]),
    ("Microbial limits", "微生物限度", ["microbial limit test", "微限"], ["DP"]),
    ("Mycoplasma", "支原体", ["mycoplasma test", "支原体检测"], ["DS"]),
    ("Adventitious agents", "外源因子", ["adventitious virus", "外源病毒", "外源因子检测"], ["DS"]),
    ("Host-cell proteins", "宿主细胞蛋白（HCP）", ["hcp", "host cell protein", "宿主蛋白"], ["DS"]),
    ("Residual host-cell DNA", "残留宿主细胞 DNA", ["residual dna", "hcdna", "残留dna"], ["DS"]),
    ("Residual Protein A", "残留 Protein A", ["protein a", "proa", "残留蛋白a"], ["DS"]),
    ("Residual solvents", "残留溶剂", ["solvent residues", "溶剂残留"], ["DS", "DP"]),
    ("Elemental impurities", "元素杂质", ["heavy metals", "金属杂质", "元素杂质"], ["DS", "DP"]),
    ("Nitrosamines", "亚硝胺类杂质", ["nitrosamine", "亚硝胺"], ["DS", "DP"]),
], "微生物与安全性检测 / Microbiology & Safety")

# Process-monitoring tests are not automatically filed under release specifications.
for en, zh, aliases, scope in [
    ("Viable cell density", "活细胞密度（VCD）", ["vcd", "viable cell concentration", "活细胞密度"], ["DS"]),
    ("Cell viability", "细胞活率", ["viability", "细胞存活率"], ["DS"]),
    ("Product titer", "产物滴度", ["titer", "蛋白滴度", "产量滴度"], ["DS"]),
    ("Glucose", "葡萄糖", ["glucose ipc", "葡萄糖检测"], ["DS"]),
    ("Lactate", "乳酸", ["lactic acid", "乳酸检测"], ["DS"]),
    ("Ammonia", "氨", ["ammonium", "氨浓度"], ["DS"]),
    ("Dissolved oxygen", "溶解氧（DO）", ["do", "pO2", "溶氧"], ["DS"]),
    ("Dissolved carbon dioxide", "溶解二氧化碳（pCO2）", ["pco2", "dco2", "溶解二氧化碳"], ["DS"]),
    ("Conductivity", "电导率", ["conductivity ipc", "电导"], ["DS", "DP"]),
    ("Column pool concentration", "层析收集液浓度", ["pool concentration", "收集液浓度"], ["DS"]),
    ("In-process impurity clearance", "过程杂质清除监测", ["ipc impurity", "过程杂质", "杂质清除监测"], ["DS"]),
]:
    codes = {side: (["3.2.S.2.4", "3.2.S.2.2"] if side == "DS" else ["3.2.P.3.4", "3.2.P.3.3"]) for side in scope}
    TERM_RECORDS.append(_term(en, zh, aliases, scope, "工艺中控检测 / In-process Tests", "检测项目 / Test", codes,
                              f"作为工艺中控检测监测{zh}，用于判断步骤状态、收获时点或中间体适用性。",
                              ["采样点、频率和在线/离线方式", "方法范围、速度和系统适用性", "警戒/行动限及调整规则", "与 CPP、CQA、收率和批处置的关系"], ["ICH_M4Q", "ICH_Q11"]))

# Container-closure and device-related test vocabulary.
for en, zh, aliases in [
    ("Vacuum decay", "真空衰减法", ["vacuum decay cci", "真空衰减"]),
    ("Helium leak", "氦质谱检漏", ["helium leak test", "氦检漏"]),
    ("High-voltage leak detection", "高压放电检漏（HVLD）", ["hvld", "高压检漏"]),
    ("Laser-based headspace analysis", "激光顶空分析", ["headspace cci", "激光顶空"]),
    ("Dye ingress", "染色液侵入法", ["dye penetration", "染料渗透"]),
    ("Microbial ingress", "微生物侵入法", ["microbial challenge", "微生物侵入"]),
    ("Break-loose and glide force", "启动力与滑动力", ["blgf", "break loose force", "滑动力"]),
    ("Stopper penetration and fragmentation", "胶塞穿刺力与落屑", ["penetration force", "fragmentation", "穿刺落屑"]),
    ("Residual seal force", "残余密封力（RSF）", ["rsf", "residual seal", "残余密封力"]),
]:
    TERM_RECORDS.append(_term(en, zh, aliases, ["DP"], "包材与功能性检测 / Packaging & Functionality", "检测项目 / Test",
                              {"DP": ["3.2.P.7", "3.2.P.2.4", "3.2.P.8.3"]},
                              f"用于评价容器密闭系统的{zh}，支持保护性、功能性或货架期完整性结论。",
                              ["方法选择与缺陷/泄漏限的关联", "阳性对照、检测限和系统适用性", "最差组件、装配、运输和老化条件", "结果与 CCI、无菌保证和变更评估的关系"], ["FDA_CCI", "FDA_CCS", "ICH_M4Q"]))

for en, zh, aliases, scope in [
    ("Polysorbate content", "聚山梨酯含量", ["polysorbate", "吐温含量"], ["DP"]),
    ("Polysorbate degradation", "聚山梨酯降解", ["polysorbate degradation", "吐温降解"], ["DP"]),
    ("Residual detergent", "残留去污剂", ["detergent residue", "清洁剂残留"], ["DS", "DP"]),
    ("Residual antifoam", "残留消泡剂", ["antifoam residue", "消泡剂残留"], ["DS"]),
    ("Residual antibiotics", "残留抗生素", ["antibiotic residue", "抗生素残留"], ["DS"]),
    ("Silicone oil", "硅油", ["silicone oil droplets", "硅油微滴"], ["DP"]),
]:
    codes = {side: BOTH_ANALYTICAL[side] for side in scope}
    TERM_RECORDS.append(_term(en, zh, aliases, scope, "配方与工艺残留 / Formulation & Process Residues", "检测项目 / Test", codes,
                              f"定量或监测{zh}，用于评价处方一致性、工艺清除或产品稳定性风险。", BIO_REVIEW,
                              ["ICH_M4Q", "ICH_Q2", "ICH_Q14"]))


def _concept(en, zh, aliases, scope, category, code, purpose, sources):
    codes = {side: [code[side] if isinstance(code, dict) else code] for side in scope}
    TERM_RECORDS.append(_term(en, zh, aliases, scope, category, "专用术语 / Term", codes, purpose,
                              ["定义和适用边界是否一致", "是否与风险评估及控制策略相连", "在各章节、报告和批次中的使用是否一致", "生命周期变化是否有版本与依据"], sources))


_concept("Quality Target Product Profile", "质量目标产品概况（QTPP）", ["qtpp", "质量目标"], ["DP"], "开发与控制策略 / Development & Control Strategy", "3.2.P.2.2", "对拟上市产品质量特征的前瞻性总结，是制剂开发和控制策略的起点。", ["ICH_Q8"])
_concept("Critical Quality Attribute", "关键质量属性（CQA）", ["cqa", "关键质量属性"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.6", "DP": "3.2.P.2.2"}, "需要控制在适当限度或范围内以确保产品质量的物理、化学、生物或微生物属性。", ["ICH_Q8", "ICH_Q9"])
_concept("Critical Material Attribute", "关键物料属性（CMA）", ["cma", "关键物料属性"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.3", "DP": "3.2.P.2.1"}, "可能影响 CQA 或工艺性能、需要适当控制的物料属性。", ["ICH_Q8", "ICH_Q11"])
_concept("Critical Process Parameter", "关键工艺参数（CPP）", ["cpp", "关键工艺参数"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.4", "DP": "3.2.P.3.4"}, "其变异会影响 CQA、因此需要监测或控制的工艺参数。", ["ICH_Q8", "ICH_Q11"])
_concept("Key Process Parameter", "关键过程参数（KPP）", ["kpp", "关键过程参数"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.4", "DP": "3.2.P.3.4"}, "企业常用但非统一 ICH 定义的参数等级；必须在项目中清楚定义其与 CPP 的差别。", ["ICH_Q9"])
_concept("Control strategy", "控制策略", ["overall control strategy", "控制策略"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.6", "DP": "3.2.P.2.3"}, "由产品和工艺理解形成的一组有计划控制，用于保证工艺性能和产品质量。", ["ICH_Q8", "ICH_Q10", "ICH_Q11"])
_concept("Design space", "设计空间", ["design space", "设计空间"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.6", "DP": "3.2.P.2.3"}, "已证明可保证质量的多维物料属性和工艺参数组合与交互范围。", ["ICH_Q8"])
_concept("Proven acceptable range", "已验证可接受范围（PAR）", ["par", "proven acceptable range", "可接受范围"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.6", "DP": "3.2.P.2.3"}, "针对单一参数研究得到的可接受范围，不等同于多变量设计空间。", ["ICH_Q8"])
_concept("Normal operating range", "正常操作范围（NOR）", ["nor", "normal operating range", "正常运行范围"], ["DS", "DP"], "开发与控制策略 / Development & Control Strategy", {"DS": "3.2.S.2.4", "DP": "3.2.P.3.4"}, "日常生产目标操作范围，通常位于批准或验证范围内。", ["ICH_Q8"])
_concept("Analytical Target Profile", "分析目标概况（ATP）", ["atp", "analytical target profile", "分析目标"], ["DS", "DP"], "分析生命周期 / Analytical Lifecycle", {"DS": "3.2.S.4.2", "DP": "3.2.P.5.2"}, "以预定用途和性能标准描述分析程序目标。", ["ICH_Q14", "ICH_Q2"])
_concept("Method Operable Design Region", "方法可操作设计区域（MODR）", ["modr", "method design space", "方法设计空间"], ["DS", "DP"], "分析生命周期 / Analytical Lifecycle", {"DS": "3.2.S.4.2", "DP": "3.2.P.5.2"}, "分析参数组合能够满足方法性能标准的多维区域。", ["ICH_Q14"])
_concept("System suitability test", "系统适用性试验（SST）", ["sst", "system suitability", "系统适用性"], ["DS", "DP"], "分析生命周期 / Analytical Lifecycle", {"DS": "3.2.S.4.2", "DP": "3.2.P.5.2"}, "在样品检测前或期间确认分析系统性能可接受。", ["ICH_Q2", "ICH_Q14"])
_concept("Critical reagent", "关键试剂", ["critical reagent", "关键试剂"], ["DS", "DP"], "分析生命周期 / Analytical Lifecycle", {"DS": "3.2.S.4.2", "DP": "3.2.P.5.2"}, "其批次或性能变化可能显著影响生物分析方法结果的试剂。", ["ICH_Q2", "ICH_Q14"])
_concept("Platform knowledge", "平台知识", ["platform knowledge", "平台经验"], ["DS", "DP"], "知识与风险管理 / Knowledge & Risk", {"DS": "3.2.S.2.6", "DP": "3.2.P.2.3"}, "来自同类产品或平台工艺、可经相关性论证用于当前产品的知识。", ["ICH_Q8", "ICH_Q11"])
_concept("Prior knowledge", "先验知识", ["prior knowledge", "先验经验"], ["DS", "DP"], "知识与风险管理 / Knowledge & Risk", {"DS": "3.2.S.2.6", "DP": "3.2.P.2.3"}, "开发前或开发过程中可用于风险评估和研究设计的历史、科学或平台信息。", ["ICH_Q8", "ICH_Q11"])
_concept("Established Conditions", "既定条件（ECs）", ["established conditions", "ecs", "既定条件"], ["DS", "DP"], "生命周期管理 / Lifecycle Management", {"DS": "3.2.S.2.2", "DP": "3.2.P.3.3"}, "依法变更通常需要监管沟通的产品生产和控制要素。", ["ICH_Q12"])
_concept("Post-Approval Change Management Protocol", "批准后变更管理方案（PACMP）", ["pacmp", "post approval change", "批准后变更方案"], ["DS", "DP"], "生命周期管理 / Lifecycle Management", {"DS": "3.2.S.2.6", "DP": "3.2.P.2.3"}, "预先约定未来变更、研究和报告类别的监管工具。", ["ICH_Q12"])
_concept("Bracketing", "括号法", ["bracketing", "括号设计"], ["DS", "DP"], "稳定性设计 / Stability Design", {"DS": "3.2.S.7.2", "DP": "3.2.P.8.2"}, "仅测试某些设计因素极端水平并推断中间水平的稳定性简化设计。", ["ICH_Q1"])
_concept("Matrixing", "矩阵法", ["matrixing", "矩阵设计"], ["DS", "DP"], "稳定性设计 / Stability Design", {"DS": "3.2.S.7.2", "DP": "3.2.P.8.2"}, "在各时间点测试样品总组合的选定子集的稳定性设计。", ["ICH_Q1"])



# Pilot: distinguish ingredient identity from product-specific evidence.
for number in (80, 20):
    name = f"Polysorbate {number}"
    record = _term(name, f"聚山梨酯 {number}（PS{number}）",
        [f"ps{number}", f"ps {number}", f"polysorbate{number}", f"吐温{number}", f"tween {number}"],
        ["DP"], "处方辅料 / Formulation Excipients", "专用术语 / Term",
        {"DP": ["3.2.P.2.1", "3.2.P.2.2", "3.2.P.4.1"]},
        "处方辅料主题入口：关联辅料选择、用量研究、含量控制及稳定性评价；具体功能应由产品开发证据支持。",
        ["说明辅料功能与选择依据", "论证浓度及物料质量属性", "检查与产品、其他组分的相容性", "关联开发结论、控制策略与货架期数据"],
        ["ICH_Q8", "ICH_M4Q"])
    record["ra_insight"] = {
        "申报目的": "解释为何选用该辅料、浓度如何确定，以及哪些属性需要控制。",
        "评价的风险": "辅料选择、用量或质量变化可能影响产品性能；具体失效模式应通过产品研究识别。",
        "支持的结论": "开发与相容性数据可支持处方选择及控制策略的科学依据。",
        "证据边界": "名称或既往使用记录不能单独证明当前产品的安全性、适用浓度或货架期功能。",
        "监管关注的原因": "ICH Q8(R2) 第一部分 2.1.2 关注辅料功能、浓度及其对产品性能的影响。",
        "IND 阶段": "结合临床阶段提供处方选择、适用性和风险控制依据，明确待补充研究。",
        "BLA 阶段": "结合商业处方与代表性数据，完善物料控制、处方论证及货架期证据。",
        "来源与解释性质": "依据：ICH Q8(R2) 第一部分 2.1.2、2.2.1。以上为 RA 编写的原则性解释，并非 PS80/PS20 专项强制检测清单。"
    }
    record["review_en"] = ["Justify excipient selection, function and concentration.", "Assess compatibility and relevant material attributes.", "Link development evidence to controls and shelf-life performance."]
    TERM_RECORDS.append(record)

for record in TERM_RECORDS:
    if record["name"] in ("Polysorbate content", "Polysorbate degradation"):
        record["aliases"] += ["ps80含量", "ps20含量"] if record["name"] == "Polysorbate content" else ["ps80降解", "ps20降解"]
        record["ra_insight"] = {
            "申报目的": "含量研究支持处方一致性评价；降解研究支持稳定性理解与控制策略制定。",
            "评价的风险": "评价辅料含量或组成变化是否影响产品质量，风险应结合产品数据确认。",
            "支持的结论": "适用方法与代表性数据支持所测属性的批间或时间趋势判断。",
            "证据边界": "含量结果不能单独证明辅料功能保持、全部降解物受控或产品整体稳定；研究不自动等于常规放行必检项目。",
            "监管关注的原因": "需要解释辅料在货架期内的功能，并建立适合产品的稳定性评价组合。",
            "IND 阶段": "按阶段和风险建立方法适用性及初步趋势，记录数据缺口。",
            "BLA 阶段": "以代表性批次、方法性能和长期数据论证控制项目、限度及监测安排。",
            "来源与解释性质": "原则依据：ICH Q8(R2) 第一部分 2.1.2；ICH Q5C 第 5 节。此处为 RA 综合解释，指南未据此规定所有产品必须检测 PS80/PS20。"
        }
        record["sources"] = list(dict.fromkeys(record["sources"] + ["ICH_Q8", "ICH_Q5C"]))


for record in TERM_RECORDS:
    if record["name"] in ("Polysorbate 80", "Polysorbate 20"):
        record["basics"] = {
            "是什么 / 定义": "聚山梨酯类非离子表面活性剂，在这里属于处方辅料，而不是检测方法或活性药物成分。",
            "起什么作用": "可用于保护治疗性蛋白免受界面应力影响；是否适用、使用浓度及实际保护效果需要产品研究支持。",
            "应用场景": "蛋白、抗体或 ADC 制剂的处方筛选、辅料用量研究，以及生产、储存和操作条件下的产品质量评价。",
            "如何联系到检测": "辅料本身、含量检测与降解研究是不同概念；可分别检索“聚山梨酯含量”和“聚山梨酯降解”。",
            "阅读依据": "FDA 2023 Science Forum 聚山梨酯研究摘要介绍其在蛋白处方中的用途；研究材料不代表通用监管要求。"
        }
    elif record["name"] == "Polysorbate content":
        record["basics"] = {
            "是什么 / 定义": "测定样品中聚山梨酯含量的分析项目；应说明对象为 PS80 还是 PS20，以及方法实际测量的组分和报告单位。",
            "应用场景": "处方开发中的用量与回收评价、生产前后比较、批间一致性及稳定性趋势监测；是否列入放行标准应另行论证。",
            "如何理解结果": "结果反映方法定义下的含量，不能仅凭含量合格认定辅料功能或产品整体稳定性已得到证明。"
        }
    elif record["name"] == "Polysorbate degradation":
        record["basics"] = {
            "是什么 / 定义": "研究聚山梨酯随条件或时间发生变化的过程及其对产品质量的影响，不是单一固定检测方法。",
            "研究什么": "根据产品风险评价氧化或水解等变化，并结合相关组分、游离脂肪酸或颗粒等信息解释结果。",
            "应用场景": "处方筛选、稳定性研究及异常趋势调查；用来帮助判断辅料变化与产品质量变化是否有关。",
            "阅读依据": "FDA 2023 Science Forum 研究摘要讨论了聚山梨酯降解与颗粒形成；具体因果关系仍需产品数据确认。"
        }
    if record.get("basics"):
        record["sources"] = list(dict.fromkeys(record["sources"] + ["FDA_PS_RESEARCH"]))
