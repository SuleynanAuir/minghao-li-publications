# Minghao Li | Publications

纯静态 PDF 文档库，可部署到 GitHub Pages。无需后端、npm 或外部 CDN。

- `index.html`：文档目录，支持标题搜索。
- `readers/`：每篇 PDF 的独立全屏阅读网页，可以直接分享该 HTML 的地址。
- `additional-backup/`：原始 PDF（包括 `demo/` 子目录）。

## 发布到 GitHub Pages

1. 使用 Git 或 GitHub Desktop 将本目录的内容提交到你的 GitHub 仓库，确保 `index.html` 位于仓库根目录，PDF 和 `output/pdf/` 也需要提交。部分文件超过网页上传限制，请勿使用 GitHub 网页逐个上传。
2. 仓库 **Settings → Pages → Build and deployment**，选择 **Deploy from a branch**，选择 `main` 分支和 **/(root)**，保存。
3. 使用 GitHub Pages 给出的站点地址。项目站点通常为 `https://你的用户名.github.io/仓库名/`。
4. 在目录中打开文档，将地址栏中的 `readers/xxx.html` 链接发给访问者。

官方说明：https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

`PEANUT_Prompt_Enhanced_Ablation.pdf` 原件约 113.8 MiB，超过 GitHub 的 100 MiB 单文件限制，已通过 `.gitignore` 保留在本地而不提交。阅读页使用 `output/pdf/` 中约 1.4 MiB 的网页副本（图片降采样至 180 dpi；保留文本及全部 15 页）。其余 PDF 使用原件。更新该原件时，也需要重新生成网页副本；不要强制提交超限原件。

## 添加或替换 PDF

将文件放入 `additional-backup/`，在本目录运行 `python3 scripts/build.py`，然后提交 PDF、生成的 `index.html` 和 `readers/`。原路径不变时，阅读页地址保持不变。删除或重命名 PDF 后，请一并删除对应的旧阅读页。

## 阅读行为

阅读页用 iframe 调用浏览器内置 PDF 阅读器，翻页、缩放、搜索能力由访问者的浏览器提供。网站不会主动触发下载，但 iframe 无法强制覆盖浏览器的下载偏好；部分移动浏览器也可能无法完整嵌入预览。阅读页右下角提供“无法显示？”入口，可直接打开 PDF。

在线阅读仍需要传输 PDF 数据，但通常无需手动下载、保存并用其他应用打开。较大文件首次加载可能较慢。

为优化加载，`demo/NEXUS_demo.pdf`、`demo/Peanut_demo.pdf`、`demo/internship_report_demo.pdf` 同样使用 `output/pdf/demo/` 下的网页压缩副本（NEXUS 图片 120 dpi，另外两份 180 dpi）。原件保留本地并忽略提交。替换原件后应同时更新相应网页副本。
