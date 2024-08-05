from flask import Flask, send_file, jsonify
from flask_cors import CORS
import os
import mimetypes

app = Flask(__name__)
CORS(app)  # 启用CORS以允许跨域请求

@app.route('/api/files', methods=['GET'])
def list_files():
    directory = "../zip/"
    files = [f for f in os.listdir(directory) if f.endswith('.zip')]
    return jsonify(files)

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    directory = "../zip/"
    file_path = os.path.join(directory, filename)
    
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'

    return send_file(file_path, 
                     as_attachment=True, 
                     download_name=filename,
                     mimetype=mime_type)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
