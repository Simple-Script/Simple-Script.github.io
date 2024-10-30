import os
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FileDownloader:
    def __init__(self, master):
        self.master = master
        self.master.title("File Downloader")
        self.frame = ttk.Frame(self.master, padding="30")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.url_list = [
            "https://raw.githubusercontent.com/user/repo/branch/file1.txt",
            "https://raw.githubusercontent.com/user/repo/branch/file2.txt",
            "https://raw.githubusercontent.com/user/repo/branch/file3.txt"
        ]
        self.file_names = ["file1.txt", "file2.txt", "file3.txt"]

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=0, column=0, pady=10)

        self.label = ttk.Label(self.frame, text="")
        self.label.grid(row=1, column=0, pady=10)

        self.download_button = ttk.Button(self.frame, text="Download Files", command=self.download_files)
        self.download_button.grid(row=2, column=0, pady=10)

    def download_files(self):
        download_folder = os.path.join(os.path.expanduser("~"), "Desktop", "DownloadedFiles")
        os.makedirs(download_folder, exist_ok=True)

        for index, url in enumerate(self.url_list):
            self.label.config(text=f"Downloading: {self.file_names[index]}")
            self.master.update()
            response = requests.get(url)
            file_path = os.path.join(download_folder, self.file_names[index])
            with open(file_path, 'wb') as file:
                file.write(response.content)
            self.progress['value'] = (index + 1) / len(self.url_list) * 100
            self.master.update()

        messagebox.showinfo("Download Complete", "All files have been downloaded.")
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDownloader(root)
    root.mainloop()
