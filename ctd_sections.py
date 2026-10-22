"""Operational M4Q(R1) Module 3 bilingual section map.

M4Q(R2) is deliberately not used for filing destinations while it remains draft.
"""


def _s(code, en, zh, purpose, guides):
    return {"code": code, "en": en, "zh": zh, "purpose": purpose, "guides": guides}


CTD_SECTIONS = [
    _s("3.2.S.1.1", "Nomenclature", "命名", "名称、CAS、INN/USAN、实验室代码及其他标识。", ["M4Q"]),
    _s("3.2.S.1.2", "Structure", "结构", "结构式、序列、分子式和相对分子质量。", ["M4Q", "Q6B"]),
    _s("3.2.S.1.3", "General Properties", "一般性质", "理化、生物学性质及与功能相关的特性。", ["M4Q", "Q6B"]),
    _s("3.2.S.2.1", "Manufacturer(s)", "生产商", "生产、检测和放行场地及其职责。", ["M4Q", "Q7"]),
    _s("3.2.S.2.2", "Description of Manufacturing Process and Process Controls", "生产工艺与过程控制描述", "流程图、工艺叙述、规模、参数和过程控制。", ["M4Q", "Q11"]),
    _s("3.2.S.2.3", "Control of Materials", "物料控制", "起始物料、细胞库、培养基、树脂及其他工艺物料控制。", ["M4Q", "Q5D", "Q11"]),
    _s("3.2.S.2.4", "Controls of Critical Steps and Intermediates", "关键步骤与中间体控制", "关键步骤、IPC、中间体标准和持留条件。", ["M4Q", "Q11"]),
    _s("3.2.S.2.5", "Process Validation and/or Evaluation", "工艺验证和/或评价", "工艺验证、病毒清除、无菌步骤和复用材料验证。", ["M4Q", "Q5A", "Q7"]),
    _s("3.2.S.2.6", "Manufacturing Process Development", "生产工艺开发", "工艺演变、参数理解、规模放大和可比性。", ["M4Q", "Q8", "Q11"]),
    _s("3.2.S.3.1", "Elucidation of Structure and Other Characteristics", "结构确证与其他特性", "一级/高级结构、异质性、生物学活性及 ADC 偶联特性。", ["M4Q", "Q6B"]),
    _s("3.2.S.3.2", "Impurities", "杂质", "产品相关和工艺相关杂质的来源、命运与控制。", ["M4Q", "Q3", "Q6B"]),
    _s("3.2.S.4.1", "Specification", "质量标准", "DS 放行与复验期检测项目及接受标准。", ["M4Q", "Q6B"]),
    _s("3.2.S.4.2", "Analytical Procedures", "分析方法", "DS 检测方法原理、步骤和关键条件。", ["M4Q", "Q14"]),
    _s("3.2.S.4.3", "Validation of Analytical Procedures", "分析方法验证", "DS 方法适用性和验证证据。", ["M4Q", "Q2", "Q14"]),
    _s("3.2.S.4.4", "Batch Analyses", "批分析", "代表性 DS 批信息与检测结果。", ["M4Q", "Q6B"]),
    _s("3.2.S.4.5", "Justification of Specification", "质量标准论证", "项目、方法和限度的科学及临床依据。", ["M4Q", "Q6B"]),
    _s("3.2.S.5", "Reference Standards or Materials", "对照品或标准物质", "一级/工作对照品的来源、赋值、表征和管理。", ["M4Q", "Q6B"]),
    _s("3.2.S.6", "Container Closure System", "容器密闭系统", "DS 储存容器、材料、规格和适用性。", ["M4Q"]),
    _s("3.2.S.7.1", "Stability Summary and Conclusions", "稳定性总结与结论", "研究概述、趋势、复验期和储存条件结论。", ["M4Q", "Q1", "Q5C"]),
    _s("3.2.S.7.2", "Post-approval Stability Protocol and Commitment", "批准后稳定性方案与承诺", "承诺批、方案和生命周期计划。", ["M4Q", "Q1", "Q5C"]),
    _s("3.2.S.7.3", "Stability Data", "稳定性数据", "批次、条件、时间点、方法和结果。", ["M4Q", "Q1", "Q5C"]),
    _s("3.2.P.1", "Description and Composition of the Drug Product", "制剂描述与组成", "剂型、规格、处方组成和组分功能。", ["M4Q"]),
    _s("3.2.P.2.1", "Components of the Drug Product", "制剂组分", "DS 与辅料属性、相容性和选择依据。", ["M4Q", "Q8"]),
    _s("3.2.P.2.2", "Drug Product", "制剂", "处方开发、过量投料和关键质量属性。", ["M4Q", "Q8"]),
    _s("3.2.P.2.3", "Manufacturing Process Development", "生产工艺开发", "制剂工艺选择、演变、放大和控制策略。", ["M4Q", "Q8"]),
    _s("3.2.P.2.4", "Container Closure System", "容器密闭系统开发", "包材选择、保护性、相容性、CCI 与 E&L。", ["M4Q", "Q8"]),
    _s("3.2.P.2.5", "Microbiological Attributes", "微生物学属性", "无菌、抑菌剂、微生物限度和无菌保证开发。", ["M4Q", "Q8"]),
    _s("3.2.P.2.6", "Compatibility", "相容性", "复溶、稀释、容器、管路和给药器具相容性。", ["M4Q", "Q8"]),
    _s("3.2.P.3.1", "Manufacturer(s)", "生产商", "制剂生产、包装、检测和放行场地职责。", ["M4Q"]),
    _s("3.2.P.3.2", "Batch Formula", "批处方", "各批量组分和用量。", ["M4Q"]),
    _s("3.2.P.3.3", "Description of Manufacturing Process and Process Controls", "生产工艺与过程控制描述", "流程、工艺叙述、设备、参数和过程控制。", ["M4Q", "Q8"]),
    _s("3.2.P.3.4", "Controls of Critical Steps and Intermediates", "关键步骤与中间体控制", "关键步骤、IPC、中间体和持留时间控制。", ["M4Q", "Q8"]),
    _s("3.2.P.3.5", "Process Validation and/or Evaluation", "工艺验证和/或评价", "PPQ、无菌工艺、过滤、灭菌和冻干验证。", ["M4Q"]),
    _s("3.2.P.4.1", "Specifications", "辅料质量标准", "辅料检测项目和接受标准。", ["M4Q"]),
    _s("3.2.P.4.2", "Analytical Procedures", "辅料分析方法", "非药典或补充检测方法。", ["M4Q"]),
    _s("3.2.P.4.3", "Validation of Analytical Procedures", "辅料方法验证", "非药典辅料方法验证证据。", ["M4Q", "Q2"]),
    _s("3.2.P.4.4", "Justification of Specifications", "辅料标准论证", "项目和限度依据。", ["M4Q"]),
    _s("3.2.P.4.5", "Excipients of Human or Animal Origin", "人源或动物源辅料", "来源、病毒和 TSE/BSE 安全性。", ["M4Q", "Q5A"]),
    _s("3.2.P.4.6", "Novel Excipients", "新型辅料", "生产、表征、控制和安全性信息。", ["M4Q"]),
    _s("3.2.P.5.1", "Specification(s)", "制剂质量标准", "DP 放行与货架期检测项目和限度。", ["M4Q", "Q6B"]),
    _s("3.2.P.5.2", "Analytical Procedures", "制剂分析方法", "DP 方法原理、步骤和关键条件。", ["M4Q", "Q14"]),
    _s("3.2.P.5.3", "Validation of Analytical Procedures", "制剂方法验证", "DP 方法适用性和验证证据。", ["M4Q", "Q2", "Q14"]),
    _s("3.2.P.5.4", "Batch Analyses", "制剂批分析", "代表性 DP 批信息与检测结果。", ["M4Q", "Q6B"]),
    _s("3.2.P.5.5", "Characterisation of Impurities", "杂质表征", "制剂降解物和其他相关杂质。", ["M4Q", "Q3", "Q6B"]),
    _s("3.2.P.5.6", "Justification of Specification(s)", "制剂质量标准论证", "项目、方法和限度依据。", ["M4Q", "Q6B"]),
    _s("3.2.P.6", "Reference Standards or Materials", "对照品或标准物质", "DP 专用或交叉引用的对照品。", ["M4Q"]),
    _s("3.2.P.7", "Container Closure System", "容器密闭系统", "组件、材料、规格、图纸和适用性。", ["M4Q"]),
    _s("3.2.P.8.1", "Stability Summary and Conclusions", "稳定性总结与结论", "趋势、货架期、使用期和储存条件结论。", ["M4Q", "Q1", "Q5C"]),
    _s("3.2.P.8.2", "Post-approval Stability Protocol and Commitment", "批准后稳定性方案与承诺", "承诺批、年度方案和生命周期计划。", ["M4Q", "Q1", "Q5C"]),
    _s("3.2.P.8.3", "Stability Data", "稳定性数据", "长期、加速、应力、在用及运输相关数据。", ["M4Q", "Q1", "Q5C"]),
    _s("3.2.A.1", "Facilities and Equipment", "设施与设备", "生物制品特定设施、设备、流向和污染控制。", ["M4Q", "Q7"]),
    _s("3.2.A.2", "Adventitious Agents Safety Evaluation", "外源因子安全性评价", "病毒及其他外源因子风险、检测和清除。", ["M4Q", "Q5A", "Q5D"]),
    _s("3.2.A.3", "Excipients", "辅料附录", "适用时提供辅料补充资料。", ["M4Q"]),
    _s("3.2.R", "Regional Information", "地区性资料", "各监管区域要求的质量信息。", ["M4Q"]),
]

SECTION_BY_CODE = {item["code"]: item for item in CTD_SECTIONS}

