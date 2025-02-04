import requests
import base64

# GitHub credentials
username = 'Simple-Script'
token = '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'  # Replace with your PAT
repo = 'web-data'
branch = 'main'  # Replace with your branch name (e.g., main or master)

# API URL for creating a file
url = f'https://api.github.com/repos/Simple-Script/web-data/contents/hello.txt'

# Data for the new file
file_content = "Hello, GitHub! This is a new file created via API."

# Encode content in base64 (required by GitHub API)
encoded_content = base64.b64encode(file_content.encode()).decode()

# JSON data for creating a file
data = {
    "message": "Create a new file",  # Commit message
    "content": encoded_content,  # Base64 encoded content
    "branch": branch
}

# Make the request to the GitHub API
response = requests.put(url, json=data, auth=(username, token))

if response.status_code == 201:
    print("File created successfully!")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
