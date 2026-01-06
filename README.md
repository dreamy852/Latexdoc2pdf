# LaTeX 轉 PDF 應用程式

一個簡單易用的 Web 應用程式，可以將 LaTeX 文檔轉換為 PDF 文件。

## 功能特點

- 📝 輸入 LaTeX 文檔內容
- 📄 自動編譯並生成 PDF
- 🎨 現代化的用戶界面
- ⚡ 快速轉換
- 📚 內建範例文檔

## 安裝需求

### 1. Python 環境
- Python 3.7 或更高版本

### 2. LaTeX 發行版
您需要安裝以下其中一個 LaTeX 發行版：

**Windows:**
- [MiKTeX](https://miktex.org/download) （推薦）
- [TeX Live](https://www.tug.org/texlive/)

**macOS:**
```bash
brew install --cask mactex
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install texlive-full
```

## 安裝步驟

1. 安裝 Python 依賴套件：
```bash
pip install -r requirements.txt
```

2. 確保 `pdflatex` 命令可用：
```bash
pdflatex --version
```

如果找不到命令，請將 LaTeX 的安裝目錄添加到系統 PATH 環境變數中。

## 使用方法

1. 啟動應用程式：
```bash
python app.py
```

2. 在瀏覽器中打開：
```
http://localhost:5000
```

3. 在文字框中輸入 LaTeX 文檔內容，或點擊範例按鈕載入範例

4. 點擊「生成 PDF」按鈕

5. PDF 文件會自動下載

## 範例

應用程式內建了三種範例：
- **基本文檔**：最簡單的 LaTeX 文檔
- **數學公式**：包含數學公式的範例
- **完整文章**：包含目錄、列表等功能的完整文檔

## 注意事項

- 編譯過程可能需要一些時間，請耐心等候
- 如果編譯失敗，錯誤訊息會顯示在頁面上
- 確保 LaTeX 文檔格式正確，特別是 `\begin{document}` 和 `\end{document}` 標籤

## 技術棧

- **後端**: Flask (Python)
- **前端**: HTML, CSS, JavaScript
- **LaTeX 編譯器**: pdflatex

## 授權

MIT License

