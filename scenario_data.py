"""Practical CMC RA scenarios: scientific/RA interpretation, not reporting decisions."""
from pro_terms import _term

# English | Chinese | definition | question | risk | evidence | boundary | aliases
PROCESS = '''
Scale-down model qualification|缩小模型适用性确认|论证实验室模型能代表目标生产步骤关键行为的研究。|小试结果可以支持商业工艺吗？|模型差异造成参数或清除结论外推失真|比较设备原理、负载、混合传质、质量属性和步骤性能|相同收率不能单独证明所有质量属性具有代表性|scale down;小试模型;缩小模型
Design of experiments|试验设计（DoE）|系统安排因素组合以研究主效应和交互作用的开发方法。|参数之间有交互作用，范围怎样确定？|单因素试验遗漏交互或边界风险|因素选择、设计空间覆盖、响应、模型诊断及确认试验|统计显著不等于质量关键，多参数范围需实际验证|doe;实验设计;参数交互
Process scale-up assessment|工艺放大评估|评价规模变化对工艺行为和产品质量影响的活动。|放大后收率或质量变化如何解释？|混合、传质或时间差异改变 CQA|尺度准则、设备差异、过程轨迹、批数据和差异桥接|相同设定值不能保证不同规模的实际条件相同|scale up;工艺放大;放大失败
Technology transfer package|技术转移资料包|将产品与工艺知识、方法及控制要求传递至接收方的资料集合。|转移到另一生产团队需要交付什么？|关键知识、参数或责任在交接中丢失|差距评估、工艺方法文件、培训、确认与转移总结|文件交付完成不代表接收场地已具生产能力|tech transfer;技术转移;技术转移失败
Manufacturing site transfer|生产场地转移评估|评价场地变化对工艺、质量及申报基线的影响。|换生产场地是否需要可比性和申报？|设备环境供应链差异影响质量或承诺|场地设备差距、工艺方法转移、验证、可比性与稳定性|报告类别和实施时点需按市场及具体变化单独判断|site transfer;换场地;生产场地变更
Process parameter excursion|工艺参数超范围评估|调查实际参数超出规定范围的原因及产品影响。|参数超限但成品合格，可以接受吗？|未测量的质量影响被成品合格掩盖|偏离幅度时长、参数与 CQA 关系、批影响和补充研究|成品合格不能自动豁免参数偏离或证明无影响|parameter excursion;参数超限;参数超范围
Reprocessing and reworking assessment|返工与重新加工评估|对偏离常规路线的再次处理方案及质量影响进行评价。|这批能返工吗，是否影响申报？|新杂质、稳定性或工艺状态不确定|定义具体步骤、原因、风险、方法覆盖、批比较和稳定性|不同产品和地区对术语与适用条件不同，不能一概批准|reprocessing;reworking;返工;重新加工
Process yield reconciliation|工艺收率与物料平衡|核对步骤投入、产出、损耗及收率趋势的活动。|收率突然降低但质量合格，需要关注什么？|异常损失或计算问题提示过程失控|计算口径、取样损耗、物料平衡及质量与杂质趋势|收率异常不必然等同质量失败，需调查具体原因|yield;物料平衡;收率下降
Intermediate acceptance criteria|中间体接受标准论证|根据后续步骤需求与质量风险设定中间体判断标准。|中间体标准能否放宽？|输入波动超出下游控制能力|属性与后续步骤关系、清除能力、历史批及边界研究|最终放行标准不能直接替代中间体标准|intermediate specification;中间体标准;中间体放宽
Single-use system qualification|一次性系统适用性确认|评价一次性组件材料及系统在实际生产中的适用性。|更换一次性袋或管路要补哪些证据？|材料迁移、吸附、完整性或连接变化影响产品|接触条件、供应材料、完整性、相容性及迁移风险|供应商验证不能自动覆盖本产品接触与操作条件|single use;一次性系统;一次性袋;管路变更
Process mixing study|混合工艺研究|评价混合过程达到所需均一性且不损伤产品的研究。|放大后的混合时间该如何论证？|不均一、局部条件或剪切影响质量|装量设备、采样位置时间、均一性和质量结果|仅看终点均一不能排除过程中的局部损伤|mixing;混合时间;搅拌研究
Lyophilization cycle development|冻干工艺开发|建立冻结、一次和二次干燥条件及产品性能关系的研究。|冻干周期变更需要证明什么？|塌陷、水分或复溶质量变化|温度压力轨迹、装载位置、关键属性及稳定性|饼形良好不单独证明活性、水分和货架期满足要求|lyophilization;冻干周期;冻干塌陷
'''
QA = '''
Corrective and preventive action|纠正与预防措施（CAPA）|针对问题原因采取措施并验证效果的质量体系活动。|CAPA 关闭了，RA 还要检查什么？|措施未解决原因导致问题重复或申报结论受影响|根因、措施逻辑、受影响批与文件、有效性标准和结果|行政关闭不等于有效性得到证明|capa;纠正预防;CAPA有效性
Quality risk assessment|质量风险评估（QRM）|识别分析评价控制并复核产品质量风险的系统过程。|风险评估说低风险，就能不做研究吗？|主观评分掩盖证据不足|问题定义、科学数据、严重性不确定性、控制与复核触发|低评分不能替代必须提供的证据或科学论证|qrm;fmea;风险评估;低风险
Quality agreement|质量协议|界定委托方与受托方质量活动和沟通责任的书面安排。|CDMO 和申办方谁负责变更通知与放行？|职责空白导致漏报、延误或监督不足|变更偏差通知、数据访问、放行、分包和争议处理职责|协议不能转移各方自身的法定责任；临床阶段适用性另行确认|quality agreement;质量协议;委托责任
Data integrity assessment|数据完整性评估|评价记录是否完整一致准确并可追溯的活动。|发现原始数据缺失，该如何评估申报影响？|无法信赖数据和相关质量结论|记录生命周期、原始数据元数据、权限、异常范围和补救|补签或补录不能恢复不存在的原始证据|data integrity;数据完整性;原始数据缺失
Audit trail review|审计追踪审阅|审查电子系统记录的数据或设置变化及相关背景。|发现删除或重复进样，RA 应关注什么？|选择性报告或无解释操作影响数据可靠性|用户时间原因、原始与处理结果、调查和扩展范围|有审计追踪不等于已审阅或数据一定可信|audit trail;审计追踪;删除数据;重复进样
Document version control|文件版本与申报一致性|控制受控文件修订并核对申报内容一致性的活动。|SOP 改了，CTD 需要更新吗？|现场执行与申报描述不一致|修订前后差异、实施时间、受影响批次及承诺对照|文字修改与实质控制变化应区分，不能只看版本号|document control;文件版本;SOP变更
Regulatory commitment tracking|法规承诺跟踪|管理已向监管方承诺的研究、期限和交付状态。|稳定性或验证承诺延期怎么办？|未履行承诺或未及时沟通|承诺原文、责任期限、完成状态、延期理由和沟通方案|内部延期批准不等于监管接受延期|commitment tracking;承诺延期;法规承诺
OOS invalidation assessment|OOS结果无效化评估|评价是否有科学证据支持将异常检测结果判为无效。|复测合格可以取消原 OOS 吗？|通过复测选择性否定真实异常|明确实验室原因、原始记录、重测方案及批影响|复测合格本身不是无效化原结果的充分依据|oos invalidation;OOS无效化;复测合格
Stability excursion investigation|稳定性异常调查|调查稳定性失效或异常趋势对产品与期限的影响。|上市批稳定性出现 OOT，需要做什么？|质量漂移影响在库或已分发产品|时间点、方法、批次趋势、储存事件和期限批影响|OOT 不自动等同 OOS，也不能忽略趋势|stability oot;稳定性异常;稳定性失败
Supplier change notification|供应商变更通知评估|评价供应商材料或生产变化对本产品的影响。|供应商说等同替换，是否可直接使用？|未披露差异影响材料功能与产品|变化细节、材料属性、可比性、使用批及验证稳定性|供应商等同性声明不能代替产品特异评估|supplier change;供应商变更;等同替换
Inspection readiness assessment|检查准备与资料一致性评估|核对现场执行、原始记录和申报论证的一致性。|迎检时 RA 与 QA 需要对齐什么？|申报与现场差异削弱质量体系和数据可信度|工艺标准基线、申报批记录、验证、偏差与承诺索引|准备材料不能替代实际整改或持续合规|inspection readiness;迎检;PAI;现场检查
Quality management review|质量管理评审|管理层定期评价质量体系绩效及改进需求的活动。|重复偏差长期未解决，是否只是 QA 问题？|系统性问题缺少资源决策和升级|趋势、重复事件、资源、行动责任和效果跟踪|会议纪要不等于质量体系有效运行|management review;管理评审;重复偏差
'''


def scenario_records():
    records = []
    for group, text in [('工艺开发', PROCESS), ('QA质量体系', QA)]:
        for line in text.strip().splitlines():
            en, zh, definition, question, risk, evidence, boundary, aliases = line.split('|')
            process = group == '工艺开发'
            codes = {'DS': ['3.2.S.2.6', '3.2.S.2.4'], 'DP': ['3.2.P.2.3', '3.2.P.3.4']} if process else {'DS': ['3.2.S.4.4', '3.2.S.2.6'], 'DP': ['3.2.P.5.4', '3.2.P.2.3']}
            refs = ['ICH_Q11', 'ICH_Q8', 'FDA_PV'] if process else ['ICH_Q10', 'ICH_Q9']
            if en == 'Quality agreement':
                refs.append('FDA_QUALITY_AGREEMENTS')
            if en in ('Data integrity assessment', 'Audit trail review', 'OOS invalidation assessment'):
                refs.append('FDA_DATA_INTEGRITY')
            if en in ('Regulatory commitment tracking', 'Document version control', 'Manufacturing site transfer'):
                refs.append('ICH_Q12')
            r = _term(en, zh, aliases.split(';') + [question], ['DS', 'DP'], group + ' / RA Scenarios', '工作场景 / Scenario', codes,
                      definition, [evidence, '确认受影响产品、批次、版本、地区和实施时间', '将质量结论与申报基线和承诺对照'], refs)
            # These are conditional destinations, never mandatory QA dossier sections.
            if not process:
                r['mappings'] = {side: [(code, label, '影响相关时交叉', '仅当该事件影响相应质量结论时关联；不表示 QA 记录必须收载。') for code, label, priority, reason in rows] for side, rows in r['mappings'].items()}
            r['filing_note'] = '开发结论按资料用途进入工艺开发、过程控制或验证等相关章节；方案和原始记录按申报策略保留支持。' if process else '通常为现场 GMP/PQS 记录，没有固定独立 CTD 位置。影响申报批、工艺、标准或承诺时，在真正受影响章节说明；下列仅为条件性交叉示例。'
            r['basics'] = {'是什么 / 定义': definition, '应用场景': question}
            r['ra_insight'] = {'申报目的': '把该事项对产品质量和申报证据的影响解释清楚，识别是否需修改资料或履行沟通。', '评价的风险': risk + '。', '支持的结论': '经审阅的证据可支持对本事项范围内质量与资料影响的判断：' + evidence + '。', '证据边界': boundary + '。', '监管关注的原因': '需要确认风险受控、数据可信，并且申报描述与实际执行一致。', '来源与解释性质': '依据所列指南原则整理的场景解释，不是法规原文；不自动确定报告类别、提交时点或批准条件。'}
            r['stage_guidance'] = {'IND': {'重点': '围绕当前临床阶段评价：' + question, '证据': '记录现有临床工艺与批次，优先控制“' + risk + '”，列明缺口和补充计划。', '审阅问题': '本事项是否影响本阶段临床批质量或已提交信息？'}, 'BLA': {'重点': '与拟商业工艺、场地及申报基线对照：' + evidence, '证据': '整合正式调查或研究结论，核对验证、稳定性、控制策略和承诺的影响。', '审阅问题': '是否影响商业代表性、批准基线或上市后沟通？按市场具体判断。'}}
            r['stage_guidance_level'] = '条目级解释'
            r['review_en'] = ['Define impacted products, batches, versions and markets.', 'Review supporting evidence and remaining uncertainty.', 'Reconcile quality decisions with the submission baseline and commitments.']
            r['work_scenario'] = {'常见问题': question, 'RA判断路径': '确认变化或异常事实 → 对照相关质量风险与申报基线 → 评估证据充分性 → 与工艺、分析和 QA 形成结论 → 确认资料更新及地区沟通安排。', '需要向团队索取': evidence + '。', '需要升级讨论的情况': risk + '且证据不足，或发现已提交资料、承诺与实际执行不一致。'}
            records.append(r)
    return records
