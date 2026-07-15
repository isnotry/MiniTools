# MiniTools 设计规范 (Design Spec)

本规范定义 MiniTools 各子工具统一的视觉语言，严格对齐 **Next.js 官方默认页面（`create-next-app` 落地页 / nextjs.org）** 的设计风格。

> 关键事实：Next.js 官方视觉的「灵魂」是 **Geist 字体**（Vercel 自研，非系统字体），配色为近黑前景 `#171717` + 纯白底 + 细灰边框 `#eaeaea`。强调蓝 `#0070f3` **仅用于链接与品牌**（Logo、文档链接），**不用于按钮**——默认页的主 CTA 是「黑底白字胶囊」。本规范据此制定。

> 适用范围：本仓库下所有前端小工具（`barcode`、`mermaid-editor`、`json-formatter`、`html-to-pdf` 等）。新增工具须遵循本规范；已有工具应逐步迁移对齐。

---

## 1. 设计原则

1. **内容优先**：界面服务于功能，不堆砌装饰。
2. **克制用色**：仅一种强调蓝 `#0070f3`，且**只用于链接 / 品牌**；按钮用前景黑，其余靠中性灰阶建立层级。
3. **边框优于阴影**：用 1px 细边框划分区域，避免厚重投影。
4. **Geist 字体**：通过 CDN 引入 Geist Sans / Geist Mono（Vercel 官方字体），系统字体仅作回退；启用字体抗锯齿。
5. **一致圆角**：卡片 / 输入 8px，按钮 128px 胶囊（Next.js 默认页 CTA 形状），小元素 6px。
6. **颜色走变量**：所有色值一律通过 CSS 变量引用，组件内禁止硬编码色值（一次性例外需注释说明）。

---

## 2. 颜色 (Color Tokens)

以 CSS 变量形式定义，便于暗色模式与主题扩展。浅色为默认（`:root`），暗色由 `html.dark` 类驱动。

```css
:root {
  /* 背景与前景（Next.js 默认：近黑 #171717，非纯黑；浅底 #fafafa） */
  --background: #ffffff;
  --background-subtle: #fafafa;   /* 页面底色 / 输入框底 */
  --background-muted: #f5f5f5;    /* 卡片内分区底色 */
  --foreground: #171717;          /* 近黑，非 #000；同时是主按钮底色 */
  --foreground-secondary: #666666;
  --foreground-tertiary: #999999;

  /* 中性灰阶（边框 / 分隔） */
  --gray-200: #eaeaea;  /* 主边框（Next.js 经典灰） */
  --gray-300: #d4d4d4;
  --gray-700: #333333;

  /* 强调色：Vercel 蓝 —— 仅用于链接 / 品牌，不用于按钮 */
  --accent: #0070f3;
  --accent-hover: #0061d5;
  --accent-subtle: #f0f7ff;  /* 蓝色淡底（聚焦环 / 链接 hover 底） */

  /* 语义色（谨慎使用） */
  --danger: #d00;
  --danger-subtle: #ffe0e0;
  /* 成功 / 信息态一律复用 --accent（蓝），不另设绿或专用 success 变量 */

  /* 按钮 hover（中性灰，非蓝） */
  --button-primary-hover: #383838;     /* 亮色：略浅的黑 */
  --button-secondary-hover: #f2f2f2;   /* 亮色：浅灰底 */
}

/* 暗色模式：背景用 #0a0a0a（非纯黑）。前景变浅灰（主按钮随之变浅底深字）。 */
:root.dark {
  --background: #0a0a0a;
  --background-subtle: #111111;
  --background-muted: #1a1a1a;
  --foreground: #ededed;          /* 非纯白，降低眩光；主按钮底色 */
  --foreground-secondary: #a0a0a0;
  --foreground-tertiary: #666666;
  --gray-200: #333333;            /* 主边框在暗底上提亮 */
  --gray-300: #444444;
  --gray-700: #cccccc;
  --accent: #0070f3;
  --accent-hover: #3291ff;        /* 暗底上 hover 提亮蓝（仅链接用） */
  --accent-subtle: #0a2540;       /* 暗底上的蓝色淡底（聚焦环） */
  --danger: #ff6b6b;              /* 暗底上红色提亮 */
  --danger-subtle: #3a1d1d;
  /* 按钮 hover：亮底更浅、暗底略亮，均非蓝 */
  --button-primary-hover: #ccc;
  --button-secondary-hover: #1a1a1a;
}
```

> **关键约定**：暗色由 `<html class="dark">` 决定，不再依赖 `@media (prefers-color-scheme: dark)` 直接改 token（避免与手动切换冲突）。是否加 `.dark` 由第 9 节的切换脚本统一裁决：默认跟随系统，用户手动选择后持久化。

> **配色纪律**：`--accent` 蓝只出现在 `<a>` 链接、Logo、输入聚焦环（`box-shadow`）、以及状态/Toast 等语义场景。**任何按钮（`.btn-*`、`.file-label`、`.theme-toggle`、卡片操作按钮）一律不得用蓝**——主按钮用前景黑，描边/幽灵按钮用 `--gray-200` 灰边。

---

## 3. 字体 (Typography)

Next.js 官方使用 **Geist**（Vercel 自研字体）。单文件工具通过 Google Fonts CDN 引入，系统字体作回退：

```css
--font-sans: "Geist", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
             Roboto, Helvetica, Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
--font-mono: "Geist Mono", "Monaco", "Menlo", "Ubuntu Mono", "Consolas", monospace;
```

`<head>` 中引入（首次需联网；离线自动回退系统字体）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@100..900&family=Geist+Mono:wght@100..900&display=swap" rel="stylesheet">
```

`body` 启用抗锯齿（Next.js 默认行为）：

```css
body {
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

### 字号刻度（Geist 风格，统一用变量引用）

```css
--text-xs:  12px;   /* 极辅助（脚注/版权） */
--text-sm:  13px;   /* 帮助文字 / meta */
--text-base:14px;   /* 正文 / 标签 / 输入 */
--text-md:  16px;   /* 区块标题 h2 / 卡片标题 */
--text-lg:  20px;   /* 次级大标题 */
--text-xl:  28px;   /* 页面主标题 h1 */
```

| 用途 | 字号 | 字重 | 行高 | 字距 | 颜色 |
| --- | --- | --- | --- | --- | --- |
| 页面主标题 `h1` | `--text-xl` (28px) | 700 | 1.25 | `-0.02em` | `--foreground` |
| 区块标题 `h2` | `--text-md` (16px) | 600 | 1.4 | `-0.01em` | `--foreground` |
| 正文 / 标签 | `--text-base` (14px) | 400 | 1.6 | — | `--foreground` / `--foreground-secondary` |
| 辅助说明 / help-text | `--text-sm` (13px) | 400 | 1.5 | — | `--foreground-tertiary` |
| 代码 / 数据 | `--text-base` (14px) | 400 | 1.6 | — | `--font-mono` |

- 标题字距轻微收紧（h1 `-0.02em`、h2 `-0.01em`），这是 Geist 排版的关键观感。
- 中文混排时保证 `PingFang SC` / `Microsoft YaHei` 回退。

---

## 4. 间距 (Spacing) — 8px 栅格

```css
--space-1: 4px;
--space-2: 8px;
--space-3: 16px;
--space-4: 24px;
--space-5: 32px;
--space-6: 48px;
```

- 卡片内边距：`--space-4`（24px）。
- 区块间垂直间距：`--space-5`（32px）。
- 紧凑元素（标签/按钮内）可用 `--space-2`–`--space-3`。

---

## 5. 圆角与边框 (Radius & Border)

```css
--radius: 8px;        /* 卡片 / 输入 */
--radius-sm: 6px;     /* 小元素 */
--radius-pill: 128px; /* 按钮（Next.js 默认页 CTA 胶囊形） */
--radius-full: 9999px;
```

- 边框统一 `1px solid var(--gray-200)`（输入、卡片、描边按钮）。
- 卡片 hover：**底色微亮**（`background: var(--background-subtle)`），边框保持 `--gray-200`，**不变蓝、不变色**。
- 按钮为胶囊形（`--radius-pill`），不是 8px 直角。

---

## 6. 组件规范 (Components)

### 6.1 卡片 Card
```css
.card {
  background: var(--background);
  border: 1px solid var(--gray-200);
  border-radius: var(--radius);
  padding: var(--space-4);
}
.card:hover { background: var(--background-subtle); } /* 仅浅灰底变化，边框不变 */
```
- 不使用渐变背景、不使用重投影。

### 6.2 按钮 Button（黑底胶囊主按钮，灰边次按钮 —— 严格对齐默认页）

- **主按钮 (Primary)**：实心 `--foreground`（黑底），白字（`var(--background)`），胶囊形。**非蓝**。
- **次按钮 (Secondary)**：白底、`1px solid var(--gray-200)`、前景字；hover 浅灰底。**边框是中性灰，非蓝**。
- **幽灵按钮 (Ghost)**：白底、`1px solid var(--gray-200)`、灰字；hover 浅灰底（与次按钮视觉近似，用于更低优先级操作）。

```css
.btn {
  display: inline-flex; align-items: center; gap: 8px;
  height: 48px; padding: 0 20px;          /* 默认页 CTA 尺寸 */
  font-size: 16px; font-weight: 500; line-height: 1;
  border-radius: var(--radius-pill);      /* 胶囊 */
  border: 1px solid transparent;
  cursor: pointer;
  transition: background .2s, border-color .2s, color .2s;
}
.btn-primary   { background: var(--foreground); color: var(--background); }
.btn-primary:hover { background: var(--button-primary-hover); }
.btn-secondary { background: var(--background); color: var(--foreground); border-color: var(--gray-200); }
.btn-secondary:hover { background: var(--button-secondary-hover); }
.btn-ghost     { background: var(--background); color: var(--foreground-secondary); border-color: var(--gray-200); }
.btn-ghost:hover { background: var(--button-secondary-hover); }
.btn:disabled  { opacity: .5; cursor: not-allowed; }
```

- 暗色模式下 `.btn-primary` 自动反转为浅底（`--foreground`=#ededed）深字（`--background`=#0a0a0a），hover `#ccc`；无需写分支。
- 避免大面积位移/缩放动效，hover 仅做颜色与底色变化。
- 不使用 emoji 作为唯一语义（可辅助），按钮文案应直接描述动作（如「生成」「保存全部」「清空」）。
- 工具内紧凑场景（如工具栏小按钮）可用 `.btn-sm`：

```css
.btn-sm { height: 36px; padding: 0 14px; font-size: 14px; }
```

### 6.3 输入 Input / Textarea / Select
```css
.input, textarea, select {
  width: 100%; padding: 10px 12px;
  font-size: var(--text-base); font-family: var(--font-sans);
  color: var(--foreground); background: var(--background);
  border: 1px solid var(--gray-200); border-radius: var(--radius);
  transition: border-color .2s, box-shadow .2s;
}
.input:focus, textarea:focus, select:focus {
  outline: none; border-color: var(--accent);   /* 聚焦环可用蓝（语义：输入态） */
  box-shadow: 0 0 0 3px var(--accent-subtle);
}
```

### 6.4 链接 Link
```css
a { color: var(--accent); text-decoration: none; }   /* 蓝仅用于链接 */
a:hover { text-decoration: underline; }
```

### 6.5 提示 Toast（可选，json-formatter / html-to-pdf 已用）

固定底部居中浮现，自动消失。成功 / 信息复用蓝（`--accent`），错误用 `--danger`。

```css
.toast {
  position: fixed; left: 50%; bottom: 32px; z-index: 1200;
  transform: translateX(-50%) translateY(20px);   /* 初始下沉 + 透明 */
  opacity: 0; pointer-events: none;
  padding: 12px 20px; border-radius: var(--radius);
  font-size: var(--text-base); font-weight: 500; color: #fff;
  transition: transform .25s, opacity .25s;
}
.toast.show { transform: translateX(-50%) translateY(0); opacity: 1; }
.toast.success { background: var(--accent); }   /* 蓝 */
.toast.info    { background: var(--accent); }   /* 蓝 */
.toast.error   { background: var(--danger); }   /* 红 */
```

- 调用：`showToast('PDF 已生成', 'success')` → 加 `.show`，约 2s 后移除。
- 文字恒为白（`#fff`），与彩色底对比满足可读性。

### 6.6 空状态 Empty State
- 居中、灰色图标 + `--foreground-tertiary` 文案，无边框卡片内呈现。

### 6.7 主题切换按钮 Theme Toggle
统一放在页面右上角，圆形、细边框、跟随主题图标（浅色显示 🌙，暗色显示 ☀️）。**hover 边框用灰（`--gray-300`），不用蓝**。

```css
.theme-toggle {
  position: fixed;            /* 全屏工具：固定右上角 */
  top: 16px; right: 16px; z-index: 1100;
  width: 40px; height: 40px;
  border-radius: var(--radius-full);
  border: 1px solid var(--gray-200);
  background: var(--background); color: var(--foreground);
  font-size: 18px; cursor: pointer;
  display: inline-flex; align-items: center; justify-content: center;
  transition: background .2s, border-color .2s, transform .2s;
}
.theme-toggle:hover { border-color: var(--gray-300); transform: scale(1.05); }
/* 应用类（如 Mermaid 全屏编辑器）融入顶栏右侧时改为静态定位 */
.theme-toggle.inline { position: static; width: 36px; height: 36px; }
```

### 6.8 文件上传标签 File Label（json-formatter / html-to-pdf 已用）

用 `<label>` 包住隐藏的 `<input type="file">`，灰虚线边框 + 中性灰字，**不出现蓝**（与按钮同纪律）。

```css
.file-label {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 10px 18px;
  border: 1px dashed var(--gray-300);     /* 虚线灰边，区别于实线按钮 */
  border-radius: var(--radius);
  color: var(--foreground-secondary); font-weight: 600; font-size: 14px;
  cursor: pointer; transition: background .2s;
}
.file-label:hover { background: var(--background-subtle); }
input[type="file"] { display: none; }       /* 原生控件藏起来，仅展示 label */
```

- 文案直接描述动作（如「📂 载入 HTML 文件」「📂 载入 JSON 文件」），emoji 仅作辅助。
- 与 `.btn` 的区别：用虚线边框表达「导入」语义，圆角 8px（非胶囊）。

### 6.9 状态条 Status Bar（json-formatter 已用）

输入校验 / 操作结果的行内状态提示，左圆点 + 文案。三态：合法（蓝）、非法（红）、空闲（灰）。

```css
.status-bar {
  display: flex; align-items: center; gap: 10px;
  padding: 12px var(--space-3); border-radius: var(--radius);
  font-size: var(--text-base); font-weight: 500; margin-bottom: var(--space-3);
}
.status-valid   { background: var(--accent-subtle);     color: var(--accent); border: 1px solid var(--accent); }
.status-invalid { background: var(--danger-subtle);     color: var(--danger); border: 1px solid var(--danger); }
.status-idle    { background: var(--background-subtle); color: var(--foreground-tertiary); border: 1px solid var(--gray-200); }
.status-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.status-valid   .status-dot { background: var(--accent); }
.status-invalid .status-dot { background: var(--danger); }
```

- 合法态复用 `--accent`（蓝），与「成功不另设绿」的纪律一致；非法态用 `--danger`。
- 文案示例：`✓ JSON 合法`、`✗ 第 3 行第 12 列：Unexpected token`。

### 6.10 页面头部 Header（两种模式，二选一）

工具按形态分两类头部，**同类工具头部必须一致**：

**A. 文档型头部（居中大标题）** —— 用于 `barcode` / `json-formatter` / `html-to-pdf` 等「容器居中」的表单型工具。标题 `h1` 居中，下配副标题；主题按钮 `fixed` 在页面右上角（见 6.7）。

```css
.header { text-align: center; margin-bottom: var(--space-5); }
.header h1 { font-size: var(--text-xl); font-weight: 700; letter-spacing: -0.02em; }
.header .subtitle {
  margin-top: var(--space-2);
  font-size: var(--text-base); color: var(--foreground-secondary);
}
```

**B. 应用型头部（顶栏）** —— 用于 `mermaid-editor` 等「全屏分栏 / 带模态」的应用型工具。标题左对齐，主题按钮内联在顶栏右侧（`.theme-toggle.inline`，避免与模态关闭按钮重叠）。

```css
.header {
  display: flex; justify-content: space-between; align-items: center;
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--gray-200);
}
.header-titles h1 { font-size: var(--text-lg); font-weight: 700; letter-spacing: -0.02em; }
.header-titles .subtitle {
  margin-top: 2px;
  font-size: var(--text-sm); color: var(--foreground-secondary);
}
```

```html
<div class="header">
  <div class="header-titles">
    <h1>Mermaid 编辑器</h1>
    <p class="subtitle">实时预览 Mermaid 图表，一键导出 PNG</p>
  </div>
  <button class="theme-toggle inline" id="themeToggle" type="button">…</button>
</div>
```

- **两类头部都必须有「标题 + 副标题」结构**，副标题一句话说明工具用途。
- **标题 `h1` 一律纯文字，不加 emoji / 符号前缀**（`🔧`、`📄`、`▦` 等）——保持四个工具标题风格统一。emoji 仅允许出现在按钮 / 文件标签等辅助语义处（见 6.2 / 6.8）。
- 应用型 A 与 B 的差异仅在「居中 vs 顶栏」「h1 28px vs 20px」「主题按钮 fixed vs inline」，其余（字体、字重、字距、副标题色）保持一致。

### 6.11 图标 Icon（统一线性 SVG）

导航卡片图标、工具内装饰性图标一律使用**内联线性 SVG**，禁止混用 emoji + 符号字形（如 `▦ / ⟿ / {} / 📄` 混排会导致基线、字重、风格全部不一致）。

```html
<span class="card-icon" aria-hidden="true">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
       stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <!-- path… -->
  </svg>
</span>
```

```css
.card-icon {
  width: 44px; height: 44px;
  border-radius: var(--radius);
  background: var(--accent-subtle);  /* 蓝色淡底 */
  color: var(--accent);              /* SVG 靠 currentColor 继承强调蓝 */
  display: inline-flex; align-items: center; justify-content: center;
  margin-bottom: var(--space-3);
}
.card-icon svg { width: 24px; height: 24px; }
```

- **统一规格**：`viewBox="0 0 24 24"`、`fill="none"`、`stroke="currentColor"`、`stroke-width="2"`、圆头圆角（`stroke-linecap/linejoin="round"`）。
- **颜色靠继承**：SVG 不写死颜色，用 `currentColor` 继承容器的 `--accent`，暗色模式自动适配。
- 图标应**具象贴合语义**（条码画成粗细不一的竖条、流程图画成父节点分叉子节点、JSON 画成花括号、HTML→PDF 画成带折角文档），避免抽象符号看不出含义。
- 尺寸统一 24px；徽章容器 44px 圆角方底（`--accent-subtle`）。

---

## 7. 布局 (Layout)

- 内容容器最大宽度约 `1100px`（JSON / HTML-PDF 工具约 `1400px`），水平居中。
- 顶部 Header：分「文档型居中头」与「应用型顶栏头」两种模式，详见 6.10；一律白底、深色标题，**不使用深色背景或渐变**（顶栏头带 `1px solid var(--gray-200)` 底边）。
- 工具型页面可分区（录入区 / 预览区）为并排卡片或上下卡片，区块间留 `--space-5`。
- 网格预览用 `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`，`gap: 24px`。

---

## 8. 技术约定

- 单文件 HTML 工具：CSS / JS 内联，依赖走 CDN（首次需联网）。
- **字体**：通过 Google Fonts 引入 **Geist / Geist Mono**（见第 3 节），离线回退系统字体；必须启用字体抗锯齿。
- 颜色、字体、圆角等一律通过上面 CSS 变量引用，禁止在组件里硬编码色值（除一次性例外）。
- **配色纪律**：`--accent` 蓝只用于链接 / 品牌 / 输入聚焦环 / 语义状态；按钮一律黑底或灰边，不出现蓝。
- 已落地的参考实现：`barcode/index.html`、`mermaid-editor/index.html`、`json-formatter/index.html`、`html-to-pdf/index.html`（均含 Geist 字体、Next.js 配色、黑底胶囊按钮、暗色模式与右上角主题切换）。

---

## 9. 主题切换机制 (Theme Switching)

所有工具采用同一套「系统自动 + 手动覆盖」策略，逻辑集中在三处：

### 9.1 防闪烁（放在 `<head>`，`</style>` 之后、`<body>` 之前，同步执行）
```html
<script>
  (function () {
    try {
      var t = localStorage.getItem('theme');           // 'light' | 'dark' | null
      if (t !== 'light' && t !== 'dark') {
        t = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      if (t === 'dark') document.documentElement.classList.add('dark');
    } catch (e) {}
  })();
</script>
```

### 9.2 切换按钮（放在 `<body>` 顶部 / 顶栏右侧）
```html
<button class="theme-toggle" id="themeToggle" type="button" aria-label="切换深色 / 浅色模式" title="切换主题">
  <span class="theme-toggle-icon">🌙</span>
</button>
```
> 全屏应用（如 Mermaid 编辑器）放入顶栏右侧并加 `inline` 类，避免与模态框关闭按钮重叠。

### 9.3 切换逻辑（放在末尾 `<script>`，需在业务脚本之后以注册钩子）
```html
<script>
  (function () {
    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    function syncIcon() {
      var isDark = document.documentElement.classList.contains('dark');
      btn.querySelector('.theme-toggle-icon').textContent = isDark ? '☀️' : '🌙';
      btn.title = isDark ? '切换到浅色' : '切换到深色';
    }
    function applyTheme(t) {
      if (t === 'dark') document.documentElement.classList.add('dark');
      else document.documentElement.classList.remove('dark');
      try { localStorage.setItem('theme', t); } catch (e) {}
      syncIcon();
      if (typeof window.__onThemeChange === 'function') window.__onThemeChange(t);
    }
    btn.addEventListener('click', function () {
      applyTheme(document.documentElement.classList.contains('dark') ? 'light' : 'dark');
    });
    syncIcon();
  })();
</script>
```

### 9.4 需要随主题联动的渲染（可选钩子）
业务脚本可注册 `window.__onThemeChange = function(theme){ ... }`：
- **Mermaid 编辑器**：切换时 `mermaid.initialize({ theme: theme === 'dark' ? 'dark' : 'default' })` 后重新渲染。
- 其他仅依赖 CSS 变量的工具无需注册，变量自动生效。

### 9.5 规则
- 默认主题 = 系统 `prefers-color-scheme`；用户点击一次后，选择写入 `localStorage('theme')` 并长期生效。
- 切换仅增删 `<html>` 上的 `.dark` 类，不改变任何业务逻辑。
- 所有视觉差异必须通过 `:root` / `:root.dark` 变量解决，不写分支 CSS。
