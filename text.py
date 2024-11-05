import tkinter as tk
from tkinter import filedialog

def download_text():
    text = text_entry.get("1.0", tk.END)
    with open("output.ss", "w") as file:
        file.write(text)

app = tk.Tk()
app.title("Text File Downloader")

text_entry = tk.Text(app, height=10, width=40)
text_entry.pack()

download_button = tk.Button(app, text="Pack", command=download_text)
download_button.pack()

app.mainloop()
