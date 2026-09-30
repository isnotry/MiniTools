# MiniTools · 单文件小工具集

**简体中文** | [English](README.en.md)

![零网络请求](https://img.shields.io/badge/network%20requests-0-brightgreen)
![零构建](https://img.shields.io/badge/build-none-lightgrey)
![11 个工具](https://img.shields.io/badge/tools-11-blue)
![数据不出本机](https://img.shields.io/badge/data-local--only-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)

> 11 个纯前端小工具，每个只是一个 `index.html`，双击打开即用，图片和数据全程留在你的浏览器里。

![界面截图](https://cdn.jsdelivr.net/gh/isnotry/MiniTools@main/docs/screenshot.png)

**[在线使用](https://isnotry.github.io/MiniTools/)**

---

## 它是什么

MiniTools 是一组不用安装、不用联网、也不用起服务的网页小工具：图片切图 / 批处理 / 加水印 / 打码 / 拼图 / 抠图，以及 JSON 格式化、流程图绘制、HTML 转 PDF、表格合并、条码生成。

每个工具独占一个目录，核心只有一个 `index.html`（HTML、CSS、JavaScript 全部内联），根目录 [`index.html`](./index.html) 是工具导航页。用到的第三方库已经全部放进各自的 `vendor/` 目录，**从打开到导出，一次网络请求都不会发出**。

## 特性

- **零安装、零构建** —— 纯静态单文件，没有 Node、没有 npm、没有打包步骤，双击就跑
- **断网可用** —— Mermaid / SheetJS / JSZip / JsBarcode / Vue 3 / heic2any / html2pdf 全部本地引入，运行时零外部依赖
- **数据不出浏览器** —— 图片、表格、JSON 都在本地内存中处理，没有任何上传接口，也没有后端
- **统一设计语言** —— 全部对齐 Next.js / Geist 风格：近黑前景 `#171717`、纯白底、细灰边框、黑底胶囊主按钮
- **深浅双主题** —— 默认跟随系统 `prefers-color-scheme`，右上角按钮可手动切换并记住偏好
- **中英双语界面** —— 每个页面右上角都有 `中` / `EN` 切换，选择记在 localStorage 的 `lang`，默认跟随浏览器语言
- **覆盖日常琐事** —— 图片处理 6 款、文档与数据转换 4 款、条码生成 1 款，共 11 个工具
- **响应式** —— 卡片栅格在窄屏自动降为单列，手机上同样可用
- **工具自带文档** —— 每个工具目录里都有一份 `README.md`，说明功能、用法与依赖
- **MIT 许可** —— 随意修改与二次分发

## 快速开始

### 在线使用

点击 **[在线使用](https://isnotry.github.io/MiniTools/)** 打开工具导航页，无需安装、不用注册。

### 本地使用

下载仓库后直接打开根目录的导航页即可：

```bash
open MiniTools/index.html        # macOS
start MiniTools\index.html       # Windows
xdg-open MiniTools/index.html    # Linux
```

也可以只取其中某一个工具，它是自包含的：

```bash
git clone git@github.com:isnotry/MiniTools.git
```

## 工具一览

| 工具 | 说明 | 入口 | 文档 |
| --- | --- | --- | --- |
| 图片裁切 | 网格切图 / 智能切图 / 智能裁剪 / 选框裁切，打包 ZIP | [打开](./image-splitter/index.html) | [文档](./image-splitter/README.md) |
| 图片批处理 | 批量格式转换（HEIC / JPG / PNG / WebP）、缩放、压缩，显示原大小→新大小，最多 99 张 | [打开](./image-batch/index.html) | [文档](./image-batch/README.md) |
| 图片加水印 | 文字 / 图片水印平铺或定位，透明度、大小、旋转、间距可调 | [打开](./image-watermark/index.html) | — |
| 图片涂抹打码 | 鼠标涂抹局部马赛克 / 模糊 / 纯色遮挡，笔刷与颗粒可调，支持撤销重做 | [打开](./image-mosaic/index.html) | [文档](./image-mosaic/README.md) |
| 图片拼图 | 多张图自动等分排布拼成一张，列数 / 画幅 / 间距 / 背景可调，拖拽排序 | [打开](./image-stitch/index.html) | [文档](./image-stitch/README.md) |
| 图片抠图 | 自动识别背景色一键去背，容差 / 羽化可调，橡皮擦手动修整，导出透明 PNG | [打开](./image-cutout/index.html) | [文档](./image-cutout/README.md) |
| JSON 格式化 | 校验 / 格式化 / 压缩 JSON，自动定位错误行列，支持排序与下载 | [打开](./json-formatter/index.html) | [文档](./json-formatter/README.md) |
| 流程图编辑器 | 基于 Mermaid 的图表编辑器，实时预览，导出 PNG / SVG | [打开](./mermaid-editor/index.html) | [文档](./mermaid-editor/README.md) |
| HTML 转 PDF | 粘贴或上传 HTML，实时预览后一键导出 PDF，支持页面尺寸与边距 | [打开](./html-to-pdf/index.html) | [文档](./html-to-pdf/README.md) |
| 表格合并 | 上传两张表格，勾选匹配字段，按全 / 内 / 左 / 右连接合并，导出 xlsx | [打开](./table-merge/index.html) | [文档](./table-merge/README.md) |
| 条码生成器 | 批量生成一维条码，导出 PNG / 打包 ZIP | [打开](./barcode/index.html) | [文档](./barcode/README.md) |

## 界面说明

| 位置 | 元素 | 作用 |
| --- | --- | --- |
| 页面右上角 | 主题按钮 🌙 / ☀️ | 在浅色与暗色之间切换，选择写入 `theme`；导航页与 11 个工具页行为一致 |
| 主题按钮左侧 | 语言按钮 `中` / `EN` | 在中英之间切换，选择写入 `lang`；12 个页面共用同一套对照表 |
| 语言按钮左侧 | GitHub 加星按钮 ⭐ / Star | 跳转到仓库 `isnotry/MiniTools`；窄屏下只显示 ⭐ 图标 |
| 导航页中部 | 工具卡片 | 点击进入对应工具 |
| 导航页底部 | GitHub 开源仓库 | 打开源码仓库 |
| 工具页顶部 | 标题 + 副标题 | 副标题一句话写清这个工具做什么、是否本地处理 |
| 图片类工具中部 | Canvas 预览区 | 在真实画布上预览效果，导出时按原始分辨率输出 |
| 操作反馈 | Toast / 状态条 | 成功与信息态用前景反色，只有错误态用红色 |

## 依赖与离线策略

第三方库全部跟随工具本地化，不引用任何 CDN：

| 工具 | 本地依赖 | 体积 |
| --- | --- | --- |
| 流程图编辑器 | Mermaid | 约 3.2 MB |
| 图片批处理 | heic2any + JSZip | 约 1.4 MB |
| 表格合并 | SheetJS + Vue 3 | 约 1.0 MB |
| HTML 转 PDF | html2pdf.bundle | 约 885 KB |
| 条码生成器 | JsBarcode + JSZip | 约 155 KB |
| 图片裁切、图片加水印 | JSZip | 各约 95 KB |
| 图片抠图、图片涂抹打码、图片拼图、JSON 格式化 | 无 | 0 |

只有需要打包多个文件的工具才引 JSZip，其余全部是原生实现。

## 关键算法口径

**图片拼图 · 自动列数**（[源码](./image-stitch/index.html)）

```js
cols = Math.ceil(Math.sqrt(n * ratio));                          // ratio = 单格画幅比
cols = Math.max(1, Math.min(Math.min(n, MAX_AUTO_COLS), cols));
rows = Math.ceil(n / cols);
```

- 目标是让整幅拼图接近设定的画幅比例，而不是简单按行列堆满
- 末行不足时可选「拉伸填满（行列不等分）」或「居中留白（保持列对齐）」

**图片抠图 · 背景判定**（[源码](./image-cutout/index.html)）

```js
band = clamp(round(min(W, H) * 0.04), 2, 128);   // 只采样四条边的窄带
d    = sqrt(dr² + dg² + db²) / √3;                // 归一化到 0-255 的颜色距离
d <= t        → alpha = 0
d >= t + soft → alpha = 255
其余          → alpha = 255 * (d - t) / soft       // soft = 羽化 × 2.5 + 1
```

- 边缘像素按 4 bit 量化后做直方图统计，取频次最高的最多 3 种颜色作为背景色
- 勾选「保留主体内部同色区」时，从画面四边做一次泛洪，只有与边缘连通的候选区域才被判为背景
- 手动擦除 / 恢复记在独立的 `delta` 层里，调容差重算时不会丢失

**JSON 格式化 · 错误定位**（[源码](./json-formatter/index.html)）

```js
pos  = parseInt(/position\s+(\d+)/i.exec(err.message)[1], 10);   // 引擎给出的字符偏移
line = raw.slice(0, pos).split('\n').length;
col  = pos - raw.slice(0, pos).lastIndexOf('\n');
```

- 匹配不到 `position` 时直接显示引擎原始报错，不做二次猜测

## 数据与隐私

- 没有后端：仓库里没有任何服务端代码，也没有一处请求指向外部地址
- 文件在你的浏览器里读、在你的浏览器里改，导出走 Blob 本地下载
- 唯一写进本机的只有两项偏好：

| 存储位置 | 键 | 内容 |
| --- | --- | --- |
| localStorage | `theme` | `light` 或 `dark`，记录手动选择的主题；导航页与 11 个工具页共用同一个键 |
| localStorage | `lang` | `zh` 或 `en`，记录手动选择的界面语言；12 个页面共用同一个键 |

## 目录结构

```text
MiniTools/
├── index.html                  # 工具导航页
├── README.md                   # 本文件（中文版）
├── README.en.md                # English version
├── LICENSE                     # MIT 许可证
├── scripts/                    # 开发者自检脚本（漏翻检查）
│   └── check_i18n.py
├── docs/                       # 设计规范与 README 截图
│   ├── design.md               # 统一设计规范（Next.js / Geist 风格）
│   ├── screenshot.png          # 中文界面封面
│   └── screenshot-en.png       # 英文界面封面
├── favicon.svg                 # 站点图标
├── robots.txt                  # 搜索引擎抓取规则
├── sitemap.xml                 # 站点地图
├── image-splitter/             # 图片裁切：网格 / 智能切图 / 智能裁剪 / 选框裁切
├── image-batch/                # 图片批处理：格式转换 / 缩放 / 压缩
├── image-watermark/            # 图片加水印
├── image-mosaic/               # 图片涂抹打码
├── image-stitch/               # 图片拼图
├── image-cutout/               # 图片抠图
├── json-formatter/             # JSON 格式化与校验
├── mermaid-editor/             # 流程图编辑器
├── html-to-pdf/                # HTML 转 PDF
├── table-merge/                # 表格合并
├── barcode/                    # 批量条码生成器
├── <工具>/README.md            # 该工具的说明文档（功能 / 用法 / 依赖）
└── <工具>/vendor/              # 该工具用到的第三方库（离线可用）
```

## 设计规范

全部工具遵循 [`docs/design.md`](./docs/design.md)，要点：

- **配色** —— 近黑前景 `#171717`、纯白底、细灰边框 `#eaeaea`；强调蓝 `#0070f3` 只用于链接、聚焦环与品牌，不用于按钮
- **按钮** —— 主按钮黑底胶囊（前景反色），次按钮 / 幽灵按钮灰边
- **提示** —— Toast 成功态与信息态用前景反色，错误态是唯一的语义红
- **字体** —— 系统字体栈优先（`-apple-system` / `Segoe UI` / `PingFang SC`），不引外部字体，省掉一次网络请求
- **暗色模式** —— 由 `<html class="dark">` 驱动，`:root` 与 `:root.dark` 两套变量切换，不写分支 CSS

## 开发说明

- **中英切换怎么加** —— 每个页面 `</body>` 前都有一段 `/* ========== 中英切换 ========== */` 脚本（`<head>` 里还有一段 lang 探测）。新增工具时整段复制过去，**只替换 `MAP`（中文 → 英文对照表）与 `PAIRS`（动态拼接串的片段替换）**；页面里保留中文原文，英文只写在表里。运行时会遍历文本节点与 `placeholder` / `title` / `aria-label` 做替换，JS 动态插入的提示由 `MutationObserver` 补翻；若页面用 `alert` / `confirm`，文案要包一层 `window.mtT()`
- **漏翻检查** —— `python3 scripts/check_i18n.py <页面路径>` 会列出还没进对照表的中文（分 text / attr / js 三类），纯给开发者自己跑的离线脚本，零依赖
- **新增工具** —— 复制一个最近的零依赖工具（如 `image-mosaic/index.html`）当骨架，沿用它的 token / 卡片 / 按钮 / Toast / 主题切换，默认值风格保持一致（间距 12、外边距 16、单格 600）
- **依赖必须本地化** —— 新库放进 `<工具>/vendor/`，用相对路径引入，**不要引 CDN**，否则会破坏离线可用性
- **颜色与圆角** —— 一律引用 CSS 变量，组件内不硬编码色值；暗色走 `:root.dark`
- **防闪烁** —— 读取 `theme` 的内联脚本放在 `<head>` 里同步执行，晚一步就会闪一下白屏
- **SEO** —— 每页都有独立的 `<title>`、`<meta name="description">`、`<link rel="canonical">`、Open Graph / Twitter Card、结构化数据（JSON-LD）与面包屑导航；`robots.txt` 和 `sitemap.xml` 已提交根目录
- **本地验收** —— 在仓库根目录起静态服务后逐个打开工具看控制台（不要直接双击时用 `file://` 调试 `vendor/` 的加载）：

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory .
```

- **文档要同步** —— 新增或修改工具能力时改四处：工具页副标题、工具目录下的 `README.md`、本文件的工具表与目录结构、[`index.html`](./index.html) 的卡片描述

## 浏览器支持

| 场景 | 要求 | 已知限制 |
| --- | --- | --- |
| 全部工具 | Canvas 2D、File API、Blob 下载（Chrome / Edge / Safari / Firefox 近两年版本） | 不支持 IE 等旧内核 |
| HEIC 输入 | 浏览器本身要能解码 HEIC，转码由 heic2any 完成 | 解码失败的单张标记为错误，其余文件继续处理 |
| 流程图编辑器 | Mermaid 以本地文件加载，约 3.2 MB | 首次渲染略慢，断网不受影响 |
| HTML 转 PDF | 依赖浏览器的打印能力 | 移动端建议用系统「打印 → 存储为 PDF」 |

## 许可

[MIT](LICENSE) © 2026 isnotry
