# Tkinter HTML Viewer

import tkinter as tk
from tkinter import filedialog
import webbrowser
import os

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("SS Files", "*.ss")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        
        html_file_path = "output.ss"
        with open(html_file_path, 'w') as html_file:
            html_file.write(content)
        
        webbrowser.open('file://' + os.path.realpath(html_file_path))

root = tk.Tk()
root.title("SS File to HTML Viewer")

open_button = tk.Button(root, text="Open .ss File", command=open_file)
open_button.pack(pady=20)

root.mainloop()
