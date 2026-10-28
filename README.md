# Minghao Li | Publications

## 在线阅读链接

[访问论文库](https://suleynanauir.github.io/minghao-li-publications/) · [GitHub 仓库](https://github.com/SuleynanAuir/minghao-li-publications)

以下链接直接打开全屏阅读页；旧长链接会自动跳转。纯文本清单：[paper-links.txt](paper-links.txt)。

### 论文与研究文档

| 序号 | 文档 | 阅读链接 |
| --- | --- | --- |
| 1 | A Unified Model for Intelligent Diagnosis-Synergizing Machine Learning and Reinforcement Learning | [ai-diagnosis](https://suleynanauir.github.io/minghao-li-publications/ai-diagnosis/) |
| 2 | A co-deployment strategy of decoy bombs based on geometric field of view masking and intelligent optimization | [decoy-strategy](https://suleynanauir.github.io/minghao-li-publications/decoy-strategy/) |
| 3 | Clinical Brain Tumor Detection- Optimized Machine Learning Frameworks for MRI Diagnosis | [brain-tumor](https://suleynanauir.github.io/minghao-li-publications/brain-tumor/) |
| 4 | Construction of Motion Simulation and Optimization Model of Bench Dragon Based on Spiral Path | [bench-dragon](https://suleynanauir.github.io/minghao-li-publications/bench-dragon/) |
| 5 | Echoes of Value- How Customer Patterns Predict Profits and What the Data Say Aloud | [customer-value](https://suleynanauir.github.io/minghao-li-publications/customer-value/) |
| 6 | Forecast and Analysis of Economic Development in the Guangdong-Hong Kong-Macao Greater Bay Area | [gba-economy](https://suleynanauir.github.io/minghao-li-publications/gba-economy/) |
| 7 | From Alignment to Reasoning in Detecting Hateful Memes | [hateful-memes](https://suleynanauir.github.io/minghao-li-publications/hateful-memes/) |
| 8 | HateReasoner | [hatereasoner](https://suleynanauir.github.io/minghao-li-publications/hatereasoner/) |
| 9 | Multi-level Chess Game Design | [chess](https://suleynanauir.github.io/minghao-li-publications/chess/) |
| 10 | NEXUS | [nexus](https://suleynanauir.github.io/minghao-li-publications/nexus/) |
| 11 | NEXUS Servy | [nexus-survey](https://suleynanauir.github.io/minghao-li-publications/nexus-survey/) |
| 12 | P-ADON4PDF | [p-adon](https://suleynanauir.github.io/minghao-li-publications/p-adon/) |
| 13 | PEANUT Prompt Enhanced Ablation | [peanut](https://suleynanauir.github.io/minghao-li-publications/peanut/) |
| 14 | Unified Automatic Rigging and 4D Gaussian Reconstruction | [4d-rigging](https://suleynanauir.github.io/minghao-li-publications/4d-rigging/) |
| 15 | Unified Automatic Rigging and 4D Gaussian Reconstruction in Robust Structure partial thesis | [4d-thesis](https://suleynanauir.github.io/minghao-li-publications/4d-thesis/) |
| 16 | Unveiling the Timeworn Scars and Knowledge of Stairs | [stairs](https://suleynanauir.github.io/minghao-li-publications/stairs/) |

### 演示与汇报文档

| 序号 | 文档 | 阅读链接 |
| --- | --- | --- |
| 17 | E Deformable Gaussians General | [deformable-gaussians](https://suleynanauir.github.io/minghao-li-publications/deformable-gaussians/) |
| 18 | FYP IncPoseFree meeting | [incposefree](https://suleynanauir.github.io/minghao-li-publications/incposefree/) |
| 19 | NEXUS demo | [nexus-demo](https://suleynanauir.github.io/minghao-li-publications/nexus-demo/) |
| 20 | Peanut demo | [peanut-demo](https://suleynanauir.github.io/minghao-li-publications/peanut-demo/) |
| 21 | internship report demo | [internship](https://suleynanauir.github.io/minghao-li-publications/internship/) |

## 网站说明

纯静态 PDF 文档库，可部署到 GitHub Pages。无需后端、npm 或外部 CDN。

- `index.html`：文档目录，支持标题搜索。
- `peanut/`、`nexus/` 等短目录：独立全屏阅读页，可直接分享。
- `readers/`：旧长地址的跳转页，保留已分享链接的可用性。
- `publications.json`：文档标题、简短标识、PDF 路径和旧地址的映射。
- `additional-backup/`：原始 PDF（包括 `demo/` 子目录）。

## 发布到 GitHub Pages

1. 使用 Git 或 GitHub Desktop 将本目录的内容提交到你的 GitHub 仓库，确保 `index.html` 位于仓库根目录，PDF 和 `output/pdf/` 也需要提交。部分文件超过网页上传限制，请勿使用 GitHub 网页逐个上传。
2. 仓库 **Settings → Pages → Build and deployment**，选择 **Deploy from a branch**，选择 `main` 分支和 **/(root)**，保存。
3. 使用 GitHub Pages 给出的站点地址。项目站点通常为 `https://你的用户名.github.io/仓库名/`。
4. 在目录中打开文档，将地址栏中的短地址（如 `peanut/`）发给访问者。

官方说明：https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

`peanut.pdf` 原件约 113.8 MiB，超过 GitHub 的 100 MiB 单文件限制，已通过 `.gitignore` 保留在本地而不提交。阅读页使用 `output/pdf/` 中约 1.4 MiB 的网页副本（图片降采样至 180 dpi；保留文本及全部 15 页）。另有三份大型演示文档使用网页压缩副本，详见下文；其他 PDF 使用原件。更新该原件时，也需要重新生成网页副本；不要强制提交超限原件。

## 添加或替换 PDF

将短文件名的 PDF 放入 `additional-backup/`，并在 `publications.json` 中添加或更新记录。`id` 用作阅读页短地址，`title` 保留完整标题，`pdf` 指向文件，`legacy` 指定旧阅读页名，`category` 为 `research` 或 `demo`。

运行 `python3 scripts/build.py`，会同步生成目录、短阅读页、旧地址跳转、README 链接表和 `paper-links.txt`。提交所有相关文件；保持 `id` 不变即可保持分享链接不变。原始 PDF 文件地址已随重命名改变，兼容跳转仅针对之前分享的 HTML 阅读页。

## 阅读行为

阅读页用 iframe 调用浏览器内置 PDF 阅读器，翻页、缩放、搜索能力由访问者的浏览器提供。网站不会主动触发下载，但 iframe 无法强制覆盖浏览器的下载偏好；部分移动浏览器也可能无法完整嵌入预览。阅读页右下角提供“无法显示？”入口，可直接打开 PDF。

在线阅读仍需要传输 PDF 数据，但通常无需手动下载、保存并用其他应用打开。较大文件首次加载可能较慢。

为优化加载，`demo/nexus-demo.pdf`、`demo/peanut-demo.pdf`、`demo/internship.pdf` 同样使用 `output/pdf/demo/` 下的网页压缩副本（NEXUS 图片 120 dpi，另外两份 180 dpi）。原件保留本地并忽略提交。替换原件后应同时更新相应网页副本。
