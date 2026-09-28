# 流程图编辑器 (Mermaid Editor)

纯前端、零依赖的单文件在线图表编辑器，左侧写代码、右侧实时预览，支持缩放查看与 PNG / SVG 导出。

> 视觉风格遵循 [`../docs/design.md`](../docs/design.md) 规范（Next.js 默认风格：浅色/暗色双主题、**Geist 字体**、近黑前景 `#171717`、`#0070f3` 蓝色仅用于链接、黑底胶囊主按钮 + 灰边次按钮、细边框卡片；右上角主题切换按钮自动跟随系统并可手动覆盖）。

## 功能特性

- **实时预览**：输入防抖（500ms）自动渲染，无需手动刷新。
- **错误提示**：语法错误时在预览区上方红框显示具体报错信息。
- **全屏查看**：点击预览图打开模态框，支持 **滚轮缩放（0.1×–10×）** 与 **鼠标拖拽平移**，点击遮罩或按 `ESC` 关闭。
- **导出 PNG**：一键将当前图表保存为 PNG（白底，按 SVG viewBox 真实尺寸输出）。
- **导出 SVG**：一键保存矢量文件，补齐命名空间与固定宽高，可在 Figma / Illustrator / draw.io 中二次编辑，缩放不失真。
- **暗色模式**：默认跟随系统，顶栏右侧 🌙/☀️ 按钮手动切换并记忆偏好；切换时 Mermaid 图表主题（default/dark）同步重渲染。
- **内置示例**：首次打开自带 `graph TD` 流程图示例，便于上手。

## 技术实现

| 项目 | 说明 |
| --- | --- |
| 入口 | `index.html`（直接双击用浏览器打开即可，无需服务器/构建） |
| 渲染引擎 | [Mermaid](https://mermaid.js.org/) `10.x`（本地 `vendor/mermaid.min.js`，离线可用） |
| 编辑器 | 原生 `textarea`（浅色代码风格，无第三方编辑器库） |
| 导出 PNG | SVG → Canvas（白底）→ PNG（`canvas.toBlob` → Blob 下载） |
| 导出 SVG | 克隆 SVG → 剥离 mermaid 注入的 `max-width` → 补 `xmlns`/`xmlns:xlink` 与固定 `width`/`height` → 插入背景层 → Blob 下载 |

### 导出实现的两个要点

1. **必须剥离根节点 `style`**：mermaid 会在 `<svg>` 上写入 `style="max-width: 232.9px"`，它是给网页内联展示用的约束；若不删除，导出的 SVG 在浏览器/编辑器里打开会被强行压到该宽度。
2. **viewBox 原点可能是负值**：mermaid 通常输出 `viewBox="-8 -8 232.9 704.75"`，因此读取尺寸时只取第 3、4 项作为宽高，**保留原 viewBox 与负原点**，否则图形会整体偏移。

导出 SVG 会插入一个带 `id="background"` 的背景矩形，颜色跟随当前主题（浅色 `#ffffff` / 暗色 `#0a0a0a`），避免暗色图在白色背景下文字看不清；**不需要时直接删除该 `<rect>` 即可恢复透明背景**。

## 使用方式

1. 浏览器打开 `mermaid-editor/index.html`。
2. 在右侧「代码编辑器」输入 Mermaid 语法（支持 flowchart / sequence / class / gantt 等）。
3. 左侧预览区即时更新；出错会高亮提示。
4. 点预览图可全屏缩放查看。
5. 点 **下载 SVG** 导出矢量图，或点 **下载 PNG** 导出位图（两者文件名均为 `mermaid-<时间戳>`）。

## 目录结构

```
mermaid-editor/
├── index.html              # 全部逻辑（HTML + CSS + JS 内联）
└── vendor/mermaid.min.js   # Mermaid 渲染引擎（本地，离线可用）
```

## 参考

- Mermaid 语法文档：https://mermaid.js.org/syntax/flowchart.html
