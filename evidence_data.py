"""Reviewed batch of navigation content; interpretations are not mandatory test lists."""
from pro_terms import _term

# name, Chinese, aliases, scope, sections, definition, application, risk, BLA evidence
ROWS = [
("Sucrose", "蔗糖", ["sucrose", "蔗糖含量"], ["DP"], ["3.2.P.2.1", "3.2.P.4.1"], "糖类处方辅料；其在具体产品中的稳定作用需要实验支持。", "处方筛选、用量及相容性研究。", "辅料浓度或属性变化影响产品稳定性。", "商业处方用量依据、辅料标准与货架期性能关联。"),
("Trehalose", "海藻糖", ["trehalose", "海藻糖含量"], ["DP"], ["3.2.P.2.1", "3.2.P.4.1"], "糖类辅料，可作为蛋白制剂处方开发的候选组分。", "液体或冻干处方筛选与稳定性比较。", "处方保护不足或组分变化导致质量变化。", "论证选用理由、物料属性及商业处方的稳定性表现。"),
("Mannitol", "甘露醇", ["mannitol", "甘露醇含量"], ["DP"], ["3.2.P.2.1", "3.2.P.2.2"], "多元醇类辅料，具体功能由处方与工艺决定。", "冻干处方等场景的辅料选择及配比研究。", "辅料与处方或工艺不匹配，影响制剂性能。", "辅料功能、用量、关键属性及冻干产品性能的开发论证。"),
("Histidine buffer", "组氨酸缓冲体系", ["histidine", "组氨酸", "组氨酸盐酸盐"], ["DP"], ["3.2.P.2.1", "3.2.P.2.2"], "以组氨酸相关组分建立的处方缓冲体系。", "处方 pH、缓冲组分和浓度筛选。", "pH 或缓冲能力变化影响产品质量。", "缓冲体系选择、浓度和 pH 范围与稳定性证据一致。"),
("Poloxamer 188", "泊洛沙姆188", ["p188", "poloxamer188", "泊洛沙姆"], ["DP"], ["3.2.P.2.1", "3.2.P.4.1"], "非离子表面活性剂类辅料；其适用性须按产品论证。", "候选表面活性剂比较、用量及相容性研究。", "替代辅料无法提供所需功能或引入新的质量影响。", "选择依据、物料属性、方法与货架期功能证据。"),
("Excipient concentration optimization", "辅料浓度优化研究", ["excipient optimization", "辅料用量", "处方浓度筛选"], ["DP"], ["3.2.P.2.2", "3.2.P.2.1"], "比较不同辅料浓度对产品质量及可制造性影响的开发研究。", "确定处方目标值及可接受范围。", "仅凭经验选用量，缺乏产品适用性证据。", "最终配方、临床配方演变及用量范围均有数据解释。"),
("Excipient compatibility study", "辅料相容性研究", ["excipient compatibility", "辅料相容性"], ["DP"], ["3.2.P.2.1", "3.2.P.2.2"], "评价药物与辅料、必要时辅料之间相互影响的研究。", "处方筛选、物料替换和相关变更评估。", "组分相互作用造成质量变化。", "研究条件覆盖拟用组分和浓度，结论与最终处方及稳定性一致。"),
("Analytical procedure robustness", "分析方法稳健性", ["robustness", "耐用性", "方法稳健性"], ["DS", "DP"], ["3.2.S.4.2", "3.2.P.5.2"], "评价分析参数小幅变化对方法性能影响的研究。", "方法开发、参数控制及方法转移准备。", "日常操作变化使方法结果不可靠。", "关键方法参数、允许范围及控制措施具有开发证据。"),
("Sample solution stability", "供试品溶液稳定性", ["sample stability", "样品溶液稳定性", "进样器稳定性"], ["DS", "DP"], ["3.2.S.4.2", "3.2.P.5.2"], "评价制备后样品在规定保存和分析条件下结果能否保持适用的研究。", "确定前处理后等待时间与进样序列时限。", "样品在等待分析期间变化，导致结果偏差。", "覆盖实际样品基质、浓度、时间温度及方法操作限制。"),
("Reference standard bridging", "对照品更换桥接", ["standard bridging", "对照品桥接", "标准品更换"], ["DS", "DP"], ["3.2.S.5", "3.2.P.6"], "比较新旧对照品并建立赋值及使用连续性的研究。", "一级或工作对照品更新、效价体系维护。", "对照品变化造成检测结果或效价尺度漂移。", "新旧对照品比较、赋值依据、适用方法及后续管理方案。"),
("Commercial process control strategy", "商业工艺控制策略汇总", ["commercial control strategy", "商业控制策略"], ["DS", "DP"], ["3.2.S.2.6", "3.2.P.2.3"], "将物料、工艺、检测及监测措施与质量风险关联的证据汇总。", "上市申报中整合开发、验证与日常控制。", "单项合格但整体控制存在缺口。", "建立 CQA—物料/参数—控制措施—验证证据的可追溯关系。"),
("PPQ sampling plan", "PPQ采样与统计方案", ["ppq sampling", "验证采样方案", "PPQ统计"], ["DS", "DP"], ["3.2.S.2.5", "3.2.P.3.5"], "预先定义验证批采样位置、频率及统计评价方式的方案。", "商业工艺性能确认准备及结果解释。", "采样不足或设计偏倚使验证无法识别批内与批间变异。", "风险与工艺知识支持采样设计、接受标准和统计评价。"),
("Process validation deviation assessment", "工艺验证偏差影响评估", ["ppq deviation", "验证偏差", "PPQ偏差"], ["DS", "DP"], ["3.2.S.2.5", "3.2.P.3.5"], "评价验证期间偏差对批次、方案执行和验证结论影响的活动。", "PPQ 总结、异常处理及补充验证决策。", "异常未解决却仍宣称工艺得到确认。", "调查根因、批影响、数据有效性与补充研究支持最终结论。"),
("Continued process verification plan", "持续工艺确认计划", ["cpv plan", "持续验证计划"], ["DS", "DP"], ["3.2.S.2.5", "3.2.P.3.5"], "规定商业生产中持续监测与评价工艺状态的计划。", "从工艺确认过渡到常规商业生产。", "商业生产漂移未及时识别。", "明确属性与参数、趋势方法、信号阈值、职责及触发行动。"),
("Shelf-life specification justification", "货架期质量标准论证", ["shelf life specification", "货架期限度", "有效期标准"], ["DP"], ["3.2.P.5.6", "3.2.P.8.1"], "论证有效期内检测项目和接受标准适用性的证据。", "上市质量标准制定、放行与货架期限度比较。", "放行合格但有效期内无法维持适宜质量。", "批数据、方法变异和长期趋势支持限度及放行标准之间的关系。"),
("Post-approval stability commitment", "批准后稳定性承诺", ["stability commitment", "稳定性承诺", "承诺批"], ["DS", "DP"], ["3.2.S.7.2", "3.2.P.8.2"], "申报时说明批准后继续开展稳定性研究的方案和承诺。", "长期数据补充及商业批稳定性安排。", "后续数据和上市储存期限支持缺少明确安排。", "方案覆盖批次、条件、时间点、检测及异常处理，承诺可跟踪。"),
("Commercial batch representativeness", "商业批代表性论证", ["batch representativeness", "商业代表性", "申报批代表性"], ["DS", "DP"], ["3.2.S.4.4", "3.2.P.5.4"], "说明申报研究批次能否代表拟商业产品、工艺与规模的论证。", "汇总临床、验证、稳定性与拟商业批关系。", "以不具代表性的研究支持商业化结论。", "批用途、规模、场地、工艺及处方版本可追溯，差异有桥接依据。"),
("Analytical lifecycle monitoring", "分析方法持续性能监测", ["method monitoring", "方法持续监测"], ["DS", "DP"], ["3.2.S.4.2", "3.2.P.5.2"], "在方法常规使用中持续评价性能并管理变化的活动。", "商业检验、方法变更与持续改进。", "验证后方法性能漂移或变化未得到控制。", "明确监测指标、评价周期和异常/变更处理，与方法控制策略衔接。"),
]


def batch_records():
    result = []
    for en, zh, aliases, scope, codes, definition, use, risk, bla in ROWS:
        mapping = {side: [code for code in codes if code.startswith("3.2.S" if side == "DS" else "3.2.P")] for side in scope}
        pv = any(word in en for word in ("PPQ", "process", "validation deviation"))
        analytical = any(word in en for word in ("Analytical", "Sample solution"))
        sources = ["ICH_M4Q", "FDA_PV"] if pv else ["ICH_M4Q", "ICH_Q2", "ICH_Q14"] if analytical else ["ICH_M4Q", "ICH_Q5C"] if "stability" in en.lower() or "Shelf-life" in en else ["ICH_M4Q", "ICH_Q6B"] if "standard" in en or "representativeness" in en else ["ICH_M4Q", "ICH_Q8"]
        r = _term(en, zh, aliases, scope, "证据专题 / Evidence Topics", "专用术语 / Term", mapping, definition,
                  ["确认研究对象、预定用途和版本", "核查代表性、方法适用性及接受标准", bla, "检查结论、剩余不确定性及跨章节一致性"], sources)
        r["review_en"] = ["Confirm intended use and study scope.", "Assess representative data and method suitability.", "Check acceptance criteria, deviations and lifecycle commitments."]
        r["basics"] = {"是什么 / 定义": definition, "应用场景": use}
        r["ra_insight"] = {"申报目的": use, "评价的风险": risk, "支持的结论": bla,
                           "证据边界": "结论限于研究覆盖的产品、条件及方法；不自动构成所有产品的必做试验或固定申报要求。",
                           "监管关注的原因": "需要以可追溯证据说明产品质量及控制措施适用于拟定用途。",
                           "来源与解释性质": "人工整理的 RA 综合解释；所列指南为原则依据，具体适用性应按产品确认。"}
        r["stage_guidance"] = {
            "IND": {"重点": use, "证据": "按临床阶段和受试者风险提供已有数据、方法适用性与临床批关联，记录未完成研究及补充计划。", "审阅问题": "现有证据能否支持本阶段临床用药？关键缺口如何控制？"},
            "BLA": {"重点": bla, "证据": "整合最终处方/工艺、代表性批次、适用的方法与接受标准、偏差处理及生命周期安排。", "审阅问题": "结论是否适用于拟商业状态？与质量标准、验证及稳定性资料是否一致？"}}
        r["stage_guidance_level"] = "条目级解释"
        r["sources"] = list(dict.fromkeys(r["sources"] + ["FDA_IND_CMC", "FDA_PV"]))
        result.append(r)
    return result


def enrich_records(records):
    """Retain stage descriptions for the four pilot records only."""
    for r in records:
        insight = r.get("ra_insight", {})
        if not insight.get("IND 阶段"):
            continue
        r["stage_guidance"] = {
            stage: {"重点": insight[stage + " 阶段"],
                    "证据": "结合辅料用途、产品代表性和方法适用性提供研究依据。",
                    "审阅问题": "该辅料或相关检测的证据能否支持所选阶段的质量结论？"}
            for stage in ("IND", "BLA")
        }
        r["stage_guidance_level"] = "条目级解释"
        r["sources"] = list(dict.fromkeys(r["sources"] + ["FDA_IND_CMC"]))
