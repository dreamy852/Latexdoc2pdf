from flask import Flask, render_template, request, send_file, jsonify
import os
import subprocess
import tempfile
import shutil
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        latex_content = request.form.get('latex_content', '')
        
        if not latex_content.strip():
            return jsonify({'error': '請輸入 LaTeX 內容'}), 400
        
        # 創建臨時目錄
        with tempfile.TemporaryDirectory() as temp_dir:
            latex_file = os.path.join(temp_dir, 'document.tex')
            pdf_file = os.path.join(temp_dir, 'document.pdf')
            
            # 寫入 LaTeX 文件
            with open(latex_file, 'w', encoding='utf-8') as f:
                f.write(latex_content)
            
            # 編譯 LaTeX 到 PDF
            try:
                # 使用 pdflatex 編譯
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', temp_dir, latex_file],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode != 0:
                    error_msg = result.stderr or result.stdout
                    return jsonify({
                        'error': 'LaTeX 編譯失敗',
                        'details': error_msg
                    }), 400
                
                # 檢查 PDF 是否生成
                if not os.path.exists(pdf_file):
                    return jsonify({'error': 'PDF 生成失敗'}), 500
                
                # 返回 PDF 文件
                return send_file(
                    pdf_file,
                    mimetype='application/pdf',
                    as_attachment=True,
                    download_name=f'document_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
                )
                
            except subprocess.TimeoutExpired:
                return jsonify({'error': '編譯超時，請檢查 LaTeX 文檔'}), 500
            except FileNotFoundError:
                return jsonify({
                    'error': '未找到 pdflatex。請安裝 LaTeX 發行版（如 MiKTeX 或 TeX Live）'
                }), 500
                
    except Exception as e:
        return jsonify({'error': f'發生錯誤: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

