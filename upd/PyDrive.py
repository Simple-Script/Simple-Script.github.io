import os
import pickle
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# If modifying the file, you'll need to use this scope
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Your credentials in JSON format as a Python string (replace with your actual JSON content)
CLIENT_SECRET_JSON = '''{
  "installed": {
    "client_id": "139512770344-l3plcp4otn2pmak2lobn84rvobd094fr.apps.googleusercontent.com",
    "project_id": "pydrive-449904",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "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",
    "redirect_uris": ["http://localhost"]
  }
}'''

# Token file to store the credentials
TOKEN_FILE = 'token.pickle'

def authenticate_google_account():
    """Authenticate the user and return the API service."""
    creds = None
    # If the token.pickle file exists, use it to get the credentials
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Load the credentials JSON
            credentials_info = json.loads(CLIENT_SECRET_JSON)
            flow = InstalledAppFlow.from_client_config(credentials_info, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    # Build the Drive API service
    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file_to_drive(service, file_path, mime_type):
    """Upload a file to Google Drive."""
    file_name = os.path.basename(file_path)

    # Create a media file upload object
    media = MediaFileUpload(file_path, mimetype=mime_type)

    # Create the file metadata
    file_metadata = {
        'name': file_name
    }

    # Upload the file
    request = service.files().create(
        media_body=media,
        body=file_metadata
    )
    file = request.execute()
    print(f"File '{file_name}' uploaded successfully!")

if __name__ == '__main__':
    # Authenticate and get the Drive API service
    service = authenticate_google_account()

    # Specify the file to upload and its MIME type
    local_file_path = r'C:\Users\Kella\Desktop\test.txt'  # Your file path here
    mime_type = 'text/plain'  # MIME type for a text file

    # Upload the file
    upload_file_to_drive(service, local_file_path, mime_type)
