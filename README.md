# LaTeX to PDF Converter

A simple web application that converts LaTeX documents to PDF in your browser.

## Features

- 📝 Enter LaTeX code in the textarea
- 📄 Generate PDF instantly
- 🎨 Clean, modern UI
- ⚡ Works entirely in the browser (no server needed)
- ☁️ Deployable to Cloudflare Pages (free)

## Usage

1. Enter your LaTeX code in the textarea
2. Click "Generate PDF"
3. The PDF will be downloaded automatically

## Deployment

### Cloudflare Pages

1. Push this repository to GitHub
2. Go to Cloudflare Dashboard → Pages
3. Connect your GitHub repository
4. Deploy!

The app will work as a static site on Cloudflare Pages.

## Example LaTeX

```latex
\documentclass{article}
\begin{document}
Hello, World!

This is a LaTeX document.

Math: $E = mc^2$

Equation:
\[
\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
\]
\end{document}
```

## Limitations

- This is a browser-based converter, so it converts LaTeX to HTML first, then to PDF
- Complex LaTeX features may not be fully supported
- For full LaTeX support, use a proper LaTeX compiler