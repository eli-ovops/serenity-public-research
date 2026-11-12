# Suoha技能接入与使用

2026-10-23用户明确要求“下载下来，并且使用它”。本项目已安装完整源码并实际使用，入口为[项目SKILL](../.agents/skills/suoha-serenity-skill/SKILL.md)。源仓库suoha888/suoha-serenity-skill，固定commit `8391ab7b1bf44000dd99bf69664b8f2e03267d16`，上游v9.1.0，本地适配v1；不自动拉取main，不覆盖已审补丁。完整安装176个源文件约8.5MB，未运行上游全局安装器，未安装新Python或付费依赖。

## 使用方式

默认通过[项目入口](../tools/suoha_research.py)调用。现有解释器是`/Users/USER/.local/bin/python3.11`（本次实测3.11.15）。入口不会复制或读取环境秘密，子进程仅接受明确的公开研究环境；不运行doctor，不传private ledger，不读API Key或券商数据。所有输入/输出须在项目内，输出必须为新路径；包括lens嵌套snapshot引用也须受检。

```bash
# 单只公开数据包；不扩张同层同行，不代表完整投资决定
/Users/USER/.local/bin/python3.11 tools/suoha_research.py pack RMBS --out-dir docs/research/新的一次运行/rmbs

# 对已取得的公开snapshot做财务体检
/Users/USER/.local/bin/python3.11 tools/suoha_research.py health docs/research/新的一次运行/rmbs/snapshots/RMBS.json --out-dir docs/research/新的一次运行/health

# 上游模型复算终值，并显式给出折现桥；rate为作者假设
/Users/USER/.local/bin/python3.11 tools/suoha_research.py value docs/research/新的一次运行/lens.json --discount-rate 0.12 --out-dir docs/research/新的一次运行/value

# 校验来源、时点、TODO和研究合同，不校验个人买卖指令
/Users/USER/.local/bin/python3.11 tools/suoha_research.py validate docs/research/新的一次运行/lens.json --out-dir docs/research/新的一次运行/gate
```

实际运行须用真实新路径，示意路径不当已存在。每次先按现行准则处理最新确认现仓风险，再补新候选。涉及财务/估值研究时使用本组件复算与发现缺口；已核且未变材料可复用，数据变更重跑相应部分。默认Quick预算不限制本项目必要的全文/脚注/事件/宏观研究，不把1只试跑称全74完成。

## 已落实的适配

- 商誉未披露/提取失败保留null/na，明确披露零才可为0；原阈值保留。
- 连接器每个请求单次尝试；401/403/429停止该host，不自动重试或将Yahoo query1改为query2。缓存/来源失败继续明确标注，不自动当投资否定。
- 子进程不继承环境凭据；研究文件及嵌套snapshot须在项目内，拒绝路径穿越、环境/凭据路径和不明外部引用。
- 上游模型的未来情景终值保留在terminal.json，现值另存present-values.json，折现率及期限显式；EV-sales净债务未知不能默认零。EPS等本项目原模型不因接入工具而偷偷更换为另一估值方法。
- 上游green只代表研究层优先级，不能代替公司事件、大盘/行业、单股金额/计划风险、原模式、组合与退出。上游不输出仓位指令不妨碍本项目在独立决定层响应用户；不把“宏观不是论点失效”当继续持有的充分理由。

## 实际使用回执

**10/23后续专项已经完整完成**：[RMBS完整研究](research/serenity-rmbs-complete-20261023/REPORT.md)、[修复财务桥](research/serenity-rmbs-complete-20261023/FINANCIAL_BRIDGE.json)、[技能原生报告](research/serenity-rmbs-complete-20261023/skill-finish/RMBS-research.md)、[finish回执](research/serenity-rmbs-complete-20261023/LENS_RUN_RECEIPT.json)。已用10-Q/10-K/ASR原件修股本与错期财务、跑repaired health并填完55TODO；原`finish`完成compute/validate/render/verify，exit0，研究amber。**其后本项目原1→0退出建议经一致性审计撤回**，当前留1不加/85原护，见[纠偏](research/serenity-rmbs-complete-20261023/CONSISTENCY_CORRECTION.md)；不能把工具校验当持有/卖出优势证明。以下为接入时的初跑历史，不再表示当前停在草稿阶段。

[接入报告](research/serenity-skill-integration-20261023/REPORT.md)／[RMBS真实研究包](research/serenity-skill-integration-20261023/rmbs-live/brief.md)／[RMBS财务检查](research/serenity-skill-integration-20261023/rmbs-health/health.md)。RMBS真实pack已执行，生成定期文件摘录、底稿、健康检查和带TODO的lens草稿；草稿校验被拒是必要的证据，不是已完成买入研究。AMD历史示例仅验证复算/校验/折现功能，不能冒今天的AMD行情或建议。

取证已发现：股本截至2026-03-31过旧；部分财务从Yahoo回退，季度收入到2026-06-30而若干资产负债/现金口径仍到3月；净债务尚待原件。即使机械体检显示若干正常项，也不得据此新增买入/加仓或取消原退出。

Codex项目技能发现从下一轮起可用；本轮已通过明确读取SKILL和执行入口实际使用，不将“已注册/能被发现”冒称全74、持续监控或收益改善。现有定时任务ID20不改时间、不新增任务；未来指定运行由项目AGENTS/当前状态接续此入口。更新须重核固定版本及补丁；不自动升级或向GitHub发送内容。
