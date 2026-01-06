# HTML to PDF Converter

A simple web application that converts HTML content to PDF in your browser.

## Features

- 📝 Enter HTML code in the textarea
- 👁️ Preview HTML before converting
- 📄 Generate PDF instantly
- 🎨 Clean, modern UI
- ⚡ Works entirely in the browser (no server needed)
- ☁️ Deployable to Cloudflare Pages (free)

## Usage

1. Enter your HTML code in the textarea
2. (Optional) Click "Preview HTML" to see how it looks
3. Click "Generate PDF"
4. The PDF will be downloaded automatically

## Deployment

### Cloudflare Pages

1. Push this repository to GitHub
2. Go to Cloudflare Dashboard → Pages
3. Connect your GitHub repository
4. Deploy!

The app will work as a static site on Cloudflare Pages.

## Example HTML

```html
<h1>Hello, World!</h1>
<p>This is a sample HTML document.</p>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

## How It Works

1. HTML code is directly inserted into a hidden div element
2. html2canvas converts the HTML element to a canvas (image)
3. jsPDF converts the canvas image to a PDF file
4. The PDF is automatically downloaded

## Limitations

- Complex CSS may not render perfectly
- External resources (images, fonts) must be accessible via CORS
- Some CSS features may not be fully supported