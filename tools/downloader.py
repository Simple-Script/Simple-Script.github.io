import os
import requests
import sys
import time

def download_file(url, file_type):
    if not os.path.exists(os.path.join(os.path.expanduser("~"), "Desktop", "console downloads")):
        os.makedirs(os.path.join(os.path.expanduser("~"), "Desktop", "console downloads"))

    local_filename = os.path.join(os.path.expanduser("~"), "Desktop", "console downloads", f"placeholder.{file_type if file_type else 'unknown'}")
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        downloaded_size = 0
        start_time = time.time()

        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded_size += len(chunk)
                elapsed_time = time.time() - start_time
                speed = downloaded_size / elapsed_time if elapsed_time > 0 else 0
                progress = (downloaded_size / total_size) * 100 if total_size > 0 else 0
                print(f"\rDownload progress: {progress:.2f}% | Downloaded: {downloaded_size} bytes | Speed: {speed:.2f} bytes/sec", end='')

    print(f"\nDownload completed! File saved as: {local_filename}")

if __name__ == "__main__":
    url = input("Enter the link to download: ")
    file_type = input("Enter the file type (or hit enter for unknown): ")
    download_file(url, file_type)
