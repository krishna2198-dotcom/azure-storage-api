from flask import Flask, jsonify, request
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = BlobServiceClient.from_connection_string(
    os.getenv("AZURE_STORAGE_CONNECTION_STRING")
)
container = os.getenv("AZURE_CONTAINER_NAME")
account = os.getenv("STORAGE_ACCOUNT_NAME")

@app.route('/')
def home():
    return jsonify({"message": "Azure Blob Storage API Running!"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    blob_client = client.get_blob_client(
        container=container, blob=file.filename
    )
    blob_client.upload_blob(file, overwrite=True)
    url = f"https://{account}.blob.core.windows.net/{container}/{file.filename}"
    return jsonify({
        "message": "File uploaded successfully!",
        "filename": file.filename,
        "url": url
    })

@app.route('/files', methods=['GET'])
def list_files():
    container_client = client.get_container_client(container)
    blobs = container_client.list_blobs()
    files = [{
        "name": b.name,
        "url": f"https://{account}.blob.core.windows.net/{container}/{b.name}",
        "size": b.size
    } for b in blobs]
    return jsonify({"total_files": len(files), "files": files})

@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    blob_client = client.get_blob_client(
        container=container, blob=filename
    )
    blob_client.delete_blob()
    return jsonify({"message": f"{filename} deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)