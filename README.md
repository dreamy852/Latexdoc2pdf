# LaTeX 轉 PDF 應用程式

一個完全在瀏覽器端運行的 LaTeX 轉 PDF 轉換工具，可部署到 Cloudflare Pages（完全免費）！

## 功能特點

- 📝 輸入 LaTeX 文檔內容
- 📄 自動編譯並生成 PDF（純瀏覽器端）
- 🎨 現代化的用戶界面
- ⚡ 即時預覽
- 📚 內建範例文檔
- 🆓 完全免費，無需服務器
- ☁️ 可部署到 Cloudflare Pages

## 技術棧

- **前端**: HTML, CSS, JavaScript
- **數學渲染**: KaTeX
- **PDF 生成**: jsPDF + html2canvas
- **部署**: Cloudflare Pages（靜態網站）

## 使用方法

### 本地運行

1. 克隆或下載此項目
2. 直接用瀏覽器打開 `index.html` 文件即可

或者使用本地服務器：
```bash
# 使用 Python
python -m http.server 8000

# 使用 Node.js
npx serve .

# 使用 PHP
php -S localhost:8000
```

然後在瀏覽器中訪問 `http://localhost:8000`

### 部署到 Cloudflare Pages（免費）

1. **推送到 GitHub**
   ```bash
   git add .
   git commit -m "Update to Cloudflare Pages compatible version"
   git push
   ```

2. **在 Cloudflare Pages 中部署**
   - 前往 [Cloudflare Dashboard](https://dash.cloudflare.com/)
   - 點擊 "Pages" → "Create a project"
   - 選擇 "Connect to Git"
   - 選擇你的 GitHub 倉庫
   - 設置：
     - **Project name**: `latexdoc2pdf`（或您喜歡的名稱）
     - **Production branch**: `main`
     - **Build command**: （留空，因為是純靜態網站）
     - **Build output directory**: （留空）
   - 點擊 "Save and Deploy"

3. **完成！**
   - 幾分鐘後，您的應用就會部署完成
   - Cloudflare 會提供一個免費的 `*.pages.dev` 域名

## 範例

應用程式內建了三種範例：
- **基本文檔**：最簡單的 LaTeX 文檔
- **數學公式**：包含數學公式的範例
- **完整文章**：包含列表等功能的完整文檔

## 功能說明

### 支援的 LaTeX 語法

- 基本文檔結構（`\documentclass`, `\begin{document}`, `\end{document}`）
- 標題（`\title`, `\author`, `\date`, `\maketitle`）
- 章節（`\section`, `\subsection`, `\subsubsection`）
- 列表（`itemize`, `enumerate`）
- 數學公式（使用 KaTeX 渲染）：
  - 行內公式：`$...$` 或 `\(...\)`
  - 區塊公式：`$$...$$` 或 `\[...\]`
- 基本格式（`\textbf`, `\textit`）
- 換行（`\\`, `\newpage`）

### 限制

- 這是簡化版的 LaTeX 編譯器，主要支援基本語法
- 複雜的 LaTeX 包（如 `graphicx`、`tikz` 等）不支援
- 對於完整的 LaTeX 功能，建議使用完整的 LaTeX 發行版

## 本地開發

無需安裝任何依賴！這是一個純靜態網站，所有庫都通過 CDN 載入：

- KaTeX（數學公式渲染）
- jsPDF（PDF 生成）
- html2canvas（HTML 到 Canvas 轉換）

## 注意事項

- PDF 生成過程可能需要幾秒鐘，請耐心等候
- 大型文檔的 PDF 生成可能需要更長時間
- 瀏覽器可能會限制某些功能（如跨域資源）

## 授權

MIT License
