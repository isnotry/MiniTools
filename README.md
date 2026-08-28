# MiniTools

一组单文件前端小工具，双击即用，无需安装、无需服务器。每个工具都是一个独立的 `index.html`（HTML + CSS + JS 内联），通过浏览器直接打开即可运行。

## 特性

- **零安装**：纯静态文件，双击 `index.html` 或任一工具的 `index.html` 即可使用。
- **统一设计语言**：全部对齐 Next.js / Geist UI 风格（Geist 字体、近黑前景、黑底胶囊主按钮、细灰边框卡片），详见 [`design.md`](./design.md)。
- **双主题**：浅色 / 暗色自动跟随系统，右上角按钮可手动切换并记忆偏好。
- **本地优先**：图片、表格等数据处理均在浏览器本地完成，不上传服务器。
- **文档齐全**：每个工具配备独立文档，统一收纳在 [`docs/`](./docs) 下。

## 工具一览

| 工具 | 说明 | 入口 | 文档 |
| --- | --- | --- | --- |
| 图片裁切 | 网格切图 / 智能切图 / 智能裁剪 / 选框裁切，打包 ZIP，本地处理 | [打开](./image-splitter/index.html) | [文档](./docs/image-splitter/README.md) |
| 图片批处理 | 批量格式转换（HEIC/JPG/PNG/WebP）、缩放、压缩，显示原大小→新大小，最多 99 张 | [打开](./image-batch/index.html) | [文档](./docs/image-batch/README.md) |
| 图片加水印 | 文字 / 图片水印平铺 / 定位，透明度、大小、旋转、间距可调，实时预览 | [打开](./image-watermark/index.html) | — |
| 图片涂抹打码 | 鼠标涂抹局部马赛克 / 模糊 / 纯色遮挡，笔刷与颗粒可调，支持撤销重做 | [打开](./image-mosaic/index.html) | [文档](./docs/image-mosaic/README.md) |
| JSON 格式化 | 校验 / 格式化 / 压缩 JSON，自动定位错误行列，支持排序与下载 | [打开](./json-formatter/index.html) | [文档](./docs/json-formatter/README.md) |
| 流程图编辑器 | 基于 Mermaid.js 的图表编辑器，实时预览，导出 PNG | [打开](./mermaid-editor/index.html) | [文档](./docs/mermaid-editor/README.md) |
| HTML 转 PDF | 粘贴或上传 HTML，实时预览后一键导出 PDF，支持页面尺寸与边距 | [打开](./html-to-pdf/index.html) | [文档](./docs/html-to-pdf/README.md) |
| 表格合并 | 上传两张表格，勾选匹配字段，按全 / 内 / 左 / 右连接合并，导出 xlsx | [打开](./table-merge/index.html) | [文档](./docs/table-merge/README.md) |
| 批量条码生成器 | 批量生成一维条码（JsBarcode），导出 PNG / 打包 ZIP | [打开](./barcode/index.html) | [文档](./docs/barcode/README.md) |

## 快速开始

直接用浏览器打开根目录的 [`index.html`](./index.html) 进入工具导航页，点击任一卡片进入对应工具；也可直接打开某个工具目录下的 `index.html`。

> 部分工具依赖 CDN（JsBarcode / Mermaid / SheetJS / JSZip / html2pdf.js / Vue3 / Geist 字体等），首次使用需联网；离线时自动回退系统字体，依赖类工具功能受限。

## 目录结构

```
MiniTools/
├── index.html               # 工具导航页（引导页）
├── design.md                # 统一设计规范（Next.js / Geist 风格）
├── README.md                # 本文件
├── docs/                    # 所有工具文档
│   ├── barcode/README.md
│   ├── html-to-pdf/README.md
│   ├── image-mosaic/README.md
│   ├── image-splitter/README.md
│   ├── json-formatter/README.md
│   ├── mermaid-editor/README.md
│   └── table-merge/README.md
├── barcode/                 # 各工具本体（单文件 index.html）
│   └── index.html
├── html-to-pdf/
│   └── index.html
├── image-mosaic/           # 图片涂抹打码
│   └── index.html
├── image-splitter/
│   └── index.html
├── image-watermark/        # 图片加水印
│   └── index.html
├── json-formatter/
│   └── index.html
├── mermaid-editor/
│   └── index.html
└── table-merge/
    └── index.html
```

## 设计规范

所有工具遵循 [`design.md`](./design.md) 定义的设计规范，核心要点：

- **字体**：Geist Sans / Geist Mono（Vercel 官方字体，CDN 引入，系统字体回退）。
- **配色**：近黑前景 `#171717` + 纯白底 + 细灰边框 `#eaeaea`；强调蓝 `#0070f3` **仅用于链接 / 品牌 / 输入聚焦环**，不用于按钮。
- **按钮**：主按钮黑底胶囊（前景反色），次按钮 / 幽灵按钮灰边；Toast 成功 / 信息态用前景反色，错误态用 `--danger` 红。
- **主题**：浅色 / 暗色双主题，由 `<html class="dark">` 驱动，默认跟随系统 `prefers-color-scheme`，手动切换写入 `localStorage`。

新增工具须遵循此规范，已有工具应逐步迁移对齐。

## 技术约定

- **单文件 HTML**：CSS / JS 内联，依赖走 CDN，无需构建。
- **颜色 / 字体 / 圆角**：一律通过 CSS 变量引用，组件内禁止硬编码色值。
- **暗色模式**：通过 `:root` / `:root.dark` 变量切换，不写分支 CSS；防闪烁脚本放在 `<head>` 同步执行。
- **无后端**：所有计算与文件处理在浏览器本地完成。

## 文档

每个工具的详细说明（功能、用法、依赖、实现说明）见 [`docs/`](./docs) 下对应子目录的 `README.md`。设计规范见根目录 [`design.md`](./design.md)。
