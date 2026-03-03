# Azure Blob Storage API 🚀
A Flask REST API for uploading, listing, and deleting files 
using Azure Blob Storage.

## Live URL
https://krish-storage-api-01.azurewebsites.net

## Tech Stack
- Python 3.10
- Flask
- Azure Blob Storage
- Azure App Service

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| POST | /upload | Upload a file |
| GET | /files | List all files |
| DELETE | /files/<filename> | Delete a file |

## How to Run Locally
pip install flask azure-storage-blob python-dotenv
python app.py
