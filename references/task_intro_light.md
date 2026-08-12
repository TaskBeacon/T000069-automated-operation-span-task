# 自动化运算广度任务：复杂工作记忆容量的实验逻辑、测量证据与解释边界

工作记忆容量（working memory capacity, WMC）的测量面临一个基本困难：实验既要考察短时保持，又要再现复杂认知中保持目标与处理新信息并行发生的情形。简单广度任务主要改变待记项目数量，难以分离存储上限、注意控制与从长期记忆恢复项目等过程。运算广度任务（operation span task, OSPAN）在序列记忆之间插入算术加工，以“加工—存储”交替结构持续打断复述，由此形成复杂广度任务的代表性范式。其成绩与流体智力、注意控制和高阶认知存在稳定的群体层面联系，但单一 OSPAN 分数仍混合了算术熟练度、处理速度、序列回忆策略与测量误差（Engle et al., 1999; Unsworth et al., 2014）。因此，范式价值来自受约束的双任务操作及其跨任务共同变异，不能把总分直接等同于一个纯粹、单一的“工作记忆容量”。

自动化运算广度任务（automated operation span task, AOSPAN）进一步标准化了刺激呈现、个体化处理时限、序列回忆与自动计分，降低了实验员节奏差异，并使大样本和跨实验室测量成为可能（Unsworth et al., 2005; Redick et al., 2012）。下文围绕范式起源、试次操作、心理过程、行为与神经证据、测量学边界以及 TaskBeacon 当前实现展开。

## 1. 范式提出与理论背景

OSPAN 源于复杂广度任务对“保持期间并发加工”这一测量需求的回应。Turner 和 Engle（1989）以算术运算替代阅读加工，发现运算背景下的记忆广度仍可预测阅读理解，说明复杂广度的预测效度并不完全依赖加工材料与效标共享语言内容。此后，潜变量研究表明，复杂广度所代表的 WMC 与简单短时存储可区分，并与流体智力共享显著变异（Engle et al., 1999）。该证据支持注意控制解释：高成绩需要维持任务目标、抵抗并发运算造成的干扰，并在注意焦点切换后恢复序列信息。

上述解释后来被扩展为保持与提取的联合观点。随着集合长度增加，待记项目可能离开当前注意焦点；成绩因而同时依赖初级记忆中的主动保持和次级记忆中的受控搜索（Unsworth & Engle, 2007）。复杂广度的加工成绩与存储成绩也并非相互独立：跨任务潜变量分析显示，加工准确率与加工时间能够解释部分高阶认知差异，近期大样本结果进一步发现，较低存储成绩者更容易因 85% 加工准确率标准而被排除（Unsworth et al., 2009; Richmond et al., 2022）。因此，算术阶段不是可忽略的“干扰器”，而是界定任务有效性和样本选择的组成部分。

Unsworth 等人（2005）将 OSPAN 自动化，采用固定刺激池、随机集合长度、个体化算术时限和即时反馈。原始 AOSPAN 的内部一致性约为 .78、重测信度约为 .83，并与其他复杂广度共同负荷于 WMC 因子。自动化提升了程序可复制性，但没有消除策略差异、任务特异方差或计分方法的影响；标准化程序仍需与明确的分析模型配套。

## 2. 任务逻辑、流程与核心参数

经典 AOSPAN 通常先练习字母序列回忆，再完成 15 道算术练习，以个人正确加工时间的均值加 2.5 个标准差确定后续时限；随后进行三个短集合的联合练习。正式阶段包含 15 个集合，集合长度 3—7 各出现三次并随机排序，共呈现 75 个“运算—字母”对（Unsworth et al., 2005）。一次项目先呈现形如“(a × b) ± c”的运算，参与者心算后判断候选结果真伪；随后一个字母短暂呈现。上述序列按当前集合长度重复，集合结束后从固定字母矩阵中依呈现顺序回忆。

个体化时限与加工准确率标准共同约束速度—复述权衡。若允许参与者在算术阶段无限延迟，其可利用额外时间复述字母，存储成绩便不再具有可比含义。原始自动版用练习阶段的反应时间分布限制正式阶段的数学处理，并要求数学正确率保持在 85% 以上；反馈同时呈现字母回忆与算术表现（Unsworth et al., 2005）。集合长度的随机化则减少参与者依固定递增序列调整策略的机会。研究设计应保留算术正确率、处理反应时和超时比例，而不应只保存最终广度分数（Richmond et al., 2022）。

常见存储指标至少包括绝对广度分数与部分计分。绝对广度只累加全部项目均按正确位置回忆的集合长度，对单个错误较敏感；部分计分按正确位置上的项目数或比例给分，保留集合内部信息。大样本比较显示，部分计分通常具有更高的内部一致性、重测相关和跨复杂广度相关，除非理论问题明确要求“整组完整保持”，否则更适合作为连续个体差异指标（Conway et al., 2005; Redick et al., 2012）。项目反应的项目反应理论分析也表明，不同集合长度和项目位置的信息量并不相等，原始总分不能自动满足等距测量假设（Draheim et al., 2018）。

各阶段对应的心理构念需要通过操作和对比加以限定。算术求解与真伪判断主要反映加工正确性、速度和目标维持；字母呈现至下一次运算之间涉及序列编码及在干扰下的保持；集合末回忆反映顺序重建、受控提取与输出监控。集合长度效应体现存储负荷和干扰机会同步增加，不能归因于单一存储槽位。OSPAN 与其他复杂广度的共同因子更接近领域一般 WMC，而单项 OSPAN 仍保留言语材料、算术加工和策略的任务特异性（Unsworth et al., 2014）。

## 3. 主要行为与神经科学发现

### 3.1 行为表现与高阶认知

OSPAN 的核心行为发现是存储成绩与注意控制、流体推理和复杂认知之间的群体关联。潜变量设计显示，这种关联不能完全由简单短时记忆或一般处理速度解释；容量、注意控制和次级记忆提取分别贡献可区分的变异（Engle et al., 1999; Unsworth et al., 2014）。2023 年一项同时测量 OSPAN、简单与自适应数字广度、Stroop 和反眼跳的研究发现，WMC 因子与注意控制的关系强于与视觉选择性注意的关系，为“目标维持和干扰控制”解释提供了较新的任务组合证据（Kotyusov et al., 2023）。该结果仍是相关结构，不能据此断言提高 OSPAN 成绩会因果性改善一般注意控制。

加工过程本身提供了重要的解释信息。Richmond 等人（2022）在多地点复杂广度数据中发现，加工准确率较高、反应较快通常伴随更好的存储表现；严格执行 85% 标准会不成比例地排除较低 WMC 个体。若研究对象可能存在算术困难、较慢加工速度或临床功能下降，排除标准可能改变样本构成。较稳妥的做法是预先规定标准，同时报告纳入与排除后的结果，并将加工表现作为协变量或独立指标检验，而非在观察结果后调整阈值。

### 3.2 fMRI、EEG 与 fNIRS 证据

任务特异的功能磁共振成像（functional magnetic resonance imaging, fMRI）证据提示，OSPAN 相较算术控制条件不仅募集经典额顶工作记忆网络，还在编码、保持和回忆时涉及海马系统。Faraco 等人（2011）观察到双侧海马活动，并发现右后海马在 OSPAN 条件下高于算术条件；这一差异支持复杂广度中注意焦点外项目可能借助长期记忆系统，但血氧水平依赖信号（blood-oxygen-level-dependent signal, BOLD）的条件差异不能确定海马活动对成绩具有因果作用，也不能完全分离编码、保持与检索。

事件相关电位与频谱研究补充了时间进程。Scharinger 等人（2017）比较 OSPAN、n-back 与数字广度时发现，OSPAN 和 n-back 的枕顶 alpha/beta 功率变化持续时间更长，OSPAN 行为表现还与 alpha 功率变化相关；n-back 的额中 theta 和 P300 效应更突出。该模式说明不同任务虽共享工作记忆负荷，却以不同方式组合持续加工、更新与控制需求。头皮 EEG 的空间定位有限，不能将频段效应直接对应到特定皮层发生源。

近红外研究进一步展示了阶段可分性。Chen 等人（2021）在 19 名健康成人中记录额叶与顶叶功能近红外光谱（functional near-infrared spectroscopy, fNIRS），发现 OSPAN 执行、反应和静息阶段的含氧血红蛋白模式可被较高准确率地区分，并可用于预测部分认知成绩。该研究支持复杂广度阶段具有可辨别的血流动力学状态，但样本较小，分类性能也可能受阶段持续时间、运动和模型验证方式影响，尚不足以建立个体诊断指标。

## 4. 范式发展与主要应用

AOSPAN 的主要发展方向是缩短施测、远程化以及跨语言适配。简体中文版研究在 102 名大学生中报告内部一致性 α = .670；其中 86 人约 8 天后重测，重测信度为 .666，OSPAN 总广度与瑞文推理在初测和重测分别相关 .33 与 .39（梅高兴等, 2021）。这些结果支持中文大学生样本中的初步效度，也显示信度低于原始自动版；语言、算术材料、软件交互和样本范围均可能造成差异。

移动测量把复杂广度从一次性实验室测验扩展到密集重复设计。Hakun 等人（2023）将 OSPAN 等复杂广度改编为智能手机超短版，完整实验室版与超短版相关约 .40—.57；两至三次超短施测可形成较可靠的个体间估计，但单次测量及个体内短期变化的可靠性较弱。近期多范式缩短研究表明，保留早期试次的缩短任务组合可解释完整任务潜变量分数的大部分变异，并将总施测时间降低约 35%；跨范式组合优于只依赖同类任务（Monteiro et al., 2025）。这些进展适合大样本、远程和纵向研究，但缩短版需要针对个体间差异或个体内变化分别验证，不能仅凭与完整版相关较高即视为等价。

## 5. 测量效度与解释边界

OSPAN 具有较成熟的聚合效度和标准化优势，但可靠性取决于计分、试次数、能力范围与施测情境。缩短复杂广度可以保留可接受的个体差异信号，部分计分一般优于绝对计分；过度缩短仍会增加地板或天花板效应，并降低对集合长度与位置效应的估计精度（Foster et al., 2015; Monteiro et al., 2025）。在高同质样本中，能力范围受限还会压低相关和重测信度。单项任务适合提供 OSPAN 特异成绩；若研究问题指向领域一般 WMC，宜使用阅读、对称或旋转广度等多个指标建立潜变量（Redick et al., 2012）。

构念效度的另一限制来自加工—存储纠缠。算术能力较低可能降低数学正确率、延长处理时间并增加被排除概率；较高算术熟练度则减小干扰负荷。个体化时限能限制策略性延迟，却无法保证不同参与者承受相同主观负荷。策略使用也会改变成绩，例如分组、语音复述和快速刷新可能提高序列保持，而总分通常不能辨认具体策略。因而组间差异应与数学表现、反应时分布、教育背景及策略测量共同解释。

效标关联不等于诊断效度。OSPAN 与流体智力及注意控制的相关主要来自健康成人群体的个体差异研究；一个稳定的群体相关不足以支持对个人进行临床分类。重复测量还可能受到程序熟悉、刺激记忆、动机与疲劳影响。研究者应预注册主要计分、加工正确率标准、异常反应处理和重测间隔，并区分个体间排序信度与个体内变化信度。中文本土化、移动超短版和实验室完整版应分别建立常模及测量等值性，而不能共享未经检验的阈值。

## 6. TaskBeacon 中的任务实现

### 6.1 任务资源与访问入口

| 资源 | ID | 用途 | 地址 |
|---|---|---|---|
| PsychoPy 完整行为实验 | T000069 | 英文 AOSPAN 本地施测与行为数据采集 | [GitHub 源码](https://github.com/TaskBeacon/T000069-automated-operation-span-task) |
| 浏览器伴随版本 | H000069 | 与 T000069 保持试次数和行为语义一致的网页预览；浏览器事件替代本地事件接口 | [GitHub 源码](https://github.com/TaskBeacon/H000069-automated-operation-span-task) |

现有公开元数据未提供可核验的直接网页运行地址，因而浏览器版本在此作为源代码预览入口列示，不替代对具体部署环境的核验。

### 6.2 实现流程与关键参数

TaskBeacon 当前版本为英文行为任务。流程依次为说明、15 次数学练习、三个长度为 2 的联合练习集合，以及 15 个计分集合；正式集合长度 3—7 各三次并随机排序，共 75 个字母—运算项目。当前版本未设置独立的字母回忆练习。数学练习的求解反应时用于计算均值加 2.5 个总体标准差，并限制在 1—10 秒；该校准值施加于后续候选答案真伪判断，运算求解界面另有固定 10 秒上限。相较原始 AOSPAN 以个体化时限约束数学处理过程，这一时限位置调整可能改变可用于复述的时间，跨实现比较时应予说明。

联合试次中，参与者先心算并按空格进入判断，以 F 表示错误、J 表示正确；随后从 F、H、J、K、L、N、P、Q、R、S、T、Y 中抽取的字母呈现 800 ms。序列完成后，参与者按顺序键入字母，每个回忆位置最长 30 秒；集合反馈呈现 2000 ms。任务输出绝对广度（完整正确集合长度之和）、正确位置字母总数和正式阶段数学正确率，并以数学正确率不低于 85% 标记成绩有效。未发现积分兑换或金钱激励设置。

![自动化运算广度任务流程](../task_flow.png)

**图 1. TaskBeacon 自动化运算广度任务流程与参数。** 数学练习按“运算求解—候选答案判断”进行 15 次，求解反应时的均值加 2.5 个总体标准差形成后续判断时限，并截断在 1—10 秒；求解界面固定上限为 10 秒，F/J 分别映射为假/真。联合练习为三个长度 2 集合，计分阶段为长度 3、4、5、6、7 各三个集合且顺序随机。每个项目依次经历求解、真伪判断和字母呈现，字母持续 800 ms，无额外抖动间隔；一个集合内重复至目标长度后，参与者从 12 个字母中逐位置顺序回忆，每一位置反应窗为 30 秒。集合反馈持续 2000 ms，报告字母正确数与数学正确数。绝对广度累加全部位置均正确的集合长度，部分成绩累计正确位置上的字母；正式数学正确率低于 85% 时总成绩标记为无效。

该实现保留了集合长度、字母池、正式试次数、800 ms 字母呈现、绝对与位置计分及 85% 数学标准等核心特征。分析时宜同时导出字母成绩、算术正确率和求解反应时，并将当前时限实施位置作为方法变量报告，以保证与原始 AOSPAN 及其他自动化版本的可比性。

## 参考文献

Chen, T., Zhao, C., Pan, X., Qu, J., Wei, J., Li, C., Liang, Y., & Zhang, X. (2021). Decoding different working memory states during an operation span task from prefrontal fNIRS signals. *Biomedical Optics Express, 12*(6), 3495–3511. https://doi.org/10.1364/BOE.426731

Conway, A. R. A., Kane, M. J., Bunting, M. F., Hambrick, D. Z., Wilhelm, O., & Engle, R. W. (2005). Working memory span tasks: A methodological review and user’s guide. *Psychonomic Bulletin & Review, 12*(5), 769–786. https://doi.org/10.3758/BF03196772

Draheim, C., Harrison, T. L., Embretson, S. E., & Engle, R. W. (2018). What item response theory can tell us about the complex span tasks. *Psychological Assessment, 30*(1), 116–129. https://doi.org/10.1037/pas0000444

Engle, R. W., Tuholski, S. W., Laughlin, J. E., & Conway, A. R. A. (1999). Working memory, short-term memory, and general fluid intelligence: A latent-variable approach. *Journal of Experimental Psychology: General, 128*(3), 309–331. https://doi.org/10.1037/0096-3445.128.3.309

Faraco, C. C., Unsworth, N., Langley, J., Terry, D., Li, K., Zhang, D., Liu, T., & Miller, L. S. (2011). Complex span tasks and hippocampal recruitment during working memory. *NeuroImage, 55*(2), 773–787. https://doi.org/10.1016/j.neuroimage.2010.12.033

Foster, J. L., Shipstead, Z., Harrison, T. L., Hicks, K. L., Redick, T. S., & Engle, R. W. (2015). Shortened complex span tasks can reliably measure working memory capacity. *Memory & Cognition, 43*(2), 226–236. https://doi.org/10.3758/s13421-014-0461-7

Hakun, J. G., Roque, N. A., Gerver, C. R., & Cerino, E. S. (2023). Ultra-brief assessment of working memory capacity: Ambulatory assessment study using smartphones. *JMIR Formative Research, 7*, e40188. https://doi.org/10.2196/40188

Kotyusov, A. I., Kasanov, D., Kosachenko, A. I., Gashkova, A. S., Pavlov, Y. G., & Malykh, S. (2023). Working memory capacity depends on attention control, but not selective attention. *Behavioral Sciences, 13*(2), 92. https://doi.org/10.3390/bs13020092

Monteiro, F., Nascimento, L. B., Leitão, J. A., Santos, E. J. R., Rodrigues, P., Santos, I. M., Simões, F., & Nascimento, C. S. (2025). Optimizing working memory assessment: Development of shortened versions of complex spans, updating, and binding tasks. *Psychological Research, 89*(2), Article 65. https://doi.org/10.1007/s00426-025-02083-7

Redick, T. S., Broadway, J. M., Meier, M. E., Kuriakose, P. S., Unsworth, N., Kane, M. J., & Engle, R. W. (2012). Measuring working memory capacity with automated complex span tasks. *European Journal of Psychological Assessment, 28*(3), 164–171. https://doi.org/10.1027/1015-5759/a000123

Richmond, L. L., Burnett, L. K., Morrison, A. B., & Ball, B. H. (2022). Performance on the processing portion of complex working memory span tasks is related to working memory capacity estimates. *Behavior Research Methods, 54*(2), 780–794. https://doi.org/10.3758/s13428-021-01645-y

Scharinger, C., Soutschek, A., Schubert, T., & Gerjets, P. (2017). Comparison of the working memory load in n-back and working memory span tasks by means of EEG frequency band power and P300 amplitude. *Frontiers in Human Neuroscience, 11*, Article 6. https://doi.org/10.3389/fnhum.2017.00006

Turner, M. L., & Engle, R. W. (1989). Is working memory capacity task dependent? *Journal of Memory and Language, 28*(2), 127–154. https://doi.org/10.1016/0749-596X(89)90040-5

Unsworth, N., & Engle, R. W. (2007). The nature of individual differences in working memory capacity: Active maintenance in primary memory and controlled search from secondary memory. *Psychological Review, 114*(1), 104–132. https://doi.org/10.1037/0033-295X.114.1.104

Unsworth, N., Fukuda, K., Awh, E., & Vogel, E. K. (2014). Working memory and fluid intelligence: Capacity, attention control, and secondary memory retrieval. *Cognitive Psychology, 71*, 1–26. https://doi.org/10.1016/j.cogpsych.2014.01.003

Unsworth, N., Heitz, R. P., Schrock, J. C., & Engle, R. W. (2005). An automated version of the operation span task. *Behavior Research Methods, 37*(3), 498–505. https://doi.org/10.3758/BF03192720

Unsworth, N., Redick, T. S., Heitz, R. P., Broadway, J. M., & Engle, R. W. (2009). Complex working memory span tasks and higher-order cognition: A latent-variable analysis of the relationship between processing and storage. *Memory, 17*(6), 635–654. https://doi.org/10.1080/09658210902998047

梅高兴, 肖寻, 陈仕语, 苟丽娜, & 李席英. (2021). 中文版工作记忆容量测量任务——“自动化运算广度任务”的信效度检验. *贵州师范大学学报（自然科学版）, 39*(4), 98–103. https://www.labxing.com/files/lab_publications/695-1626856850-KlLaExQn.pdf
