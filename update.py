# Read and display contents of a raw.githubusercontent.com file in PowerShell

import requests

url = 'https://raw.githubusercontent.com/Simple-Script/Simple-Script.github.io/refs/heads/main/update'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")
