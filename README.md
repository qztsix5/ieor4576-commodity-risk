# IEOR 4576 — Commodity Risk Replication

Bakshi, Gao and Rossi (2019), Understanding the Sources of Risk Underlying the Cross Section of Commodity Returns.
Team: PNL MAKERS — XinYu Wu, Anvesha Churi, Zhitao Qu.

## 当前版本

仅保留按 Internet Appendix Table Internet-I 逐品种计算日期的主流程。旧严格日期版、通知月份月初下界版和范围末端平行版本已退出主流程。默认范围取表内第一个日期，范围末端保留在元数据，营业日采用美国联邦假日代理；约某日取该日，未将估算称为真实历史FND。

## 安装与手动运行

在 project 根目录：

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

选择相同 Python kernel，顺序运行 notebooks：

1. `01_futures_preparation.ipynb` — 下载/清洗期货、月收益、信号和组合。
2. `02_auxiliary_preparation.ipynb` — CFTC、VIX、国家股指、宏观数据。
3. `03_data_checks.ipynb` — 日期、同合约收益、缺失和公布日边界测试。
4. `04_overlap_validation.ipynb` — 同月同品种配对统计、误差、Internet-I/II核验。

已有原始快照时默认不联网。首次下载在01设置 RUN_DOWNLOAD=True，在02设置 RUN_NETWORK=True。WRDS 密码只由 libpq 从外部 pgpass 读取，可用 PGPASSFILE 指定路径；不要将凭据写入仓库。

等价脚本入口：

```powershell
python run_all.py --data-only --offline
```

首次下载去掉 `--offline`。定价模型尚未实现，不运行完整估计。

## 数据布局

- data/raw/wrds_contracts：按 contrcode 存放逐合约日行情、原始元数据及 SHA256/来源 sidecar。
- data/raw/auxiliary、equity_indices：官方辅助数据和国家股指原始快照。
- data/raw/paper_reference：作者附件及原始发布包，仅作 benchmark。
- data/interim：月末合约截面、清洗元数据、报价审计、作者标准化数据。
- data/processed/commodity_monthly.parquet：唯一主版本完整月度数据。
- data/processed/commodity_monthly_2000_2025.parquet：Proposal 子样本。
- data/processed/portfolios.parquet、weights.parquet：因子/资产及形成日权重。
- results/replication/overlap_validation：配对明细、排序误差、总体/逐品种基础统计。
- results/replication/tables/main：Internet-I/II及日期诊断。

原始行情、作者附件与生成结果不提交 Git。新克隆先将作者 TSV（扩展名.xls）放到 data/raw/paper_reference/FuturesReturn_to_post.xls。configs 保存样本与映射，src/project 保存计算逻辑，notebook 保存手动流程和测试，遵循 repo_hierarchy。

## 研究范围与限制

请求1969–2025（含预热），实际覆盖因品种不同；原文对照截至2011-09，Proposal为2000–2025。原始 Propane 不可得，Barley市场身份待确认；不补造完整29品种。作者收益不用于填WRDS缺失。

本版本仍有日期惯例/日历代理、缺到期日交割月末假设、合约选择与数据供应商差异。CFTC实际公布日不完整，不生成预测版；G20股指为代表性指数代理，FRED为修订后数据。高相关不代表精确复现。详见 report/data_methodology.md 和 data_collection_status.md。
