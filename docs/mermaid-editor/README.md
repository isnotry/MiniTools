# Mermaid 编辑器 (Mermaid Editor)

纯前端、零依赖的单文件在线图表编辑器，左侧写代码、右侧实时预览，支持缩放查看与 PNG 导出。

> 视觉风格遵循根目录 [`../../design.md`](../../design.md) 规范（Next.js 默认风格：浅色/暗色双主题、**Geist 字体**、近黑前景 `#171717`、`#0070f3` 蓝色仅用于链接、黑底胶囊主按钮 + 灰边次按钮、细边框卡片；右上角主题切换按钮自动跟随系统并可手动覆盖）。

## 功能特性

- **实时预览**：输入防抖（500ms）自动渲染，无需手动刷新。
- **错误提示**：语法错误时在预览区上方红框显示具体报错信息。
- **全屏查看**：点击预览图打开模态框，支持 **滚轮缩放（0.1×–10×）** 与 **鼠标拖拽平移**，点击遮罩或按 `ESC` 关闭。
- **导出 PNG**：一键将当前图表保存为 PNG（白底，按 SVG viewBox 真实尺寸输出）。
- **暗色模式**：默认跟随系统，顶栏右侧 🌙/☀️ 按钮手动切换并记忆偏好；切换时 Mermaid 图表主题（default/dark）同步重渲染。
- **内置示例**：首次打开自带 `graph TD` 流程图示例，便于上手。

## 技术实现

| 项目 | 说明 |
| --- | --- |
| 入口 | `index.html`（直接双击用浏览器打开即可，无需服务器/构建） |
| 渲染引擎 | [Mermaid](https://mermaid.js.org/) `10.x`（jsDelivr CDN） |
| 编辑器 | 原生 `textarea`（浅色代码风格，无第三方编辑器库） |
| 导出格式 | SVG → Canvas（白底）→ PNG（`toDataURL`） |

> 依赖通过 CDN 加载，首次使用需联网。

## 使用方式

1. 浏览器打开 `mermaid-editor/index.html`。
2. 在右侧「代码编辑器」输入 Mermaid 语法（支持 flowchart / sequence / class / gantt 等）。
3. 左侧预览区即时更新；出错会高亮提示。
4. 点预览图可全屏缩放查看。
5. 点 **下载 PNG** 导出当前图表。

## 目录结构

```
mermaid-editor/
└── index.html   # 全部逻辑（HTML + CSS + JS 内联）
```

## 参考

- Mermaid 语法文档：https://mermaid.js.org/syntax/flowchart.html
