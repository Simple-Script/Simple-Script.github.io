import tkinter as tk
import subprocess
import os

class FullscreenApp:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen', True)
        self.master.configure(bg='black')

        self.buttons = []
        self.button_names = [
            "Apex Legends", "Ark: Survival Ascended", "Ark: Survival Evolved", "Astroneer", "CS2",
            "Fortnite", "Forza Horizon 5", "Grounded", "Minecraft", "Minecraft Dungeons",
            "Roblox", "Rocket League", "Slime Rancher", "Trailmakers", "Valorant",
            "Empty", "Empty", "Empty", "Empty", "AMD Adrenalin"
        ]
        self.button_paths = [
            r"C:\Users\Kella\Desktop\Fortnite.url", r"C:\Users\Kella\Desktop\Roblox Player.lnk",
            r"C:\Users\YourUsername\Desktop\app3.exe", r"C:\Users\YourUsername\Desktop\app4.exe",
            r"C:\Users\YourUsername\Desktop\app5.exe", r"C:\Users\Kella\Desktop\Fortnite.url",
            r"C:\Users\YourUsername\Desktop\app7.exe", r"C:\Users\YourUsername\Desktop\app8.exe",
            r"C:\Users\YourUsername\Desktop\app9.exe", r"C:\Users\YourUsername\Desktop\app10.exe",
            r"C:\Users\Kella\Desktop\Roblox Player.lnk", r"C:\Users\YourUsername\Desktop\app12.exe",
            r"C:\Users\YourUsername\Desktop\app13.exe", r"C:\Users\YourUsername\Desktop\app14.exe",
            r"C:\Users\YourUsername\Desktop\app15.exe", r"C:\Users\YourUsername\Desktop\app16.exe",
            r"C:\Users\YourUsername\Desktop\app17.exe", r"C:\Users\YourUsername\Desktop\app18.exe",
            r"C:\Users\YourUsername\Desktop\app19.exe", r"C:\Users\YourUsername\Desktop\app20.exe"
        ]

        self.create_buttons()
        self.create_exit_button()

    def create_buttons(self):
        for i in range(4):
            for j in range(5):
                index = i * 5 + j
                button = tk.Button(self.master, text=self.button_names[index], 
                                   command=lambda path=self.button_paths[index]: self.run_exe(path),
                                   width=40, height=12, bg='gray', fg='black', font=('Arial', 16))
                button.grid(row=i, column=j, padx=10, pady=10)
                self.buttons.append(button)

    def create_exit_button(self):
        exit_button = tk.Button(self.master, text="Exit to Desktop", command=self.master.quit,
                                width=211, height=4, bg='red', fg='white', font=('Arial', 16))
        exit_button.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

    def run_exe(self, path):
        if os.path.exists(path):
            subprocess.Popen(path)

if __name__ == "__main__":
    root = tk.Tk()
    app = FullscreenApp(root)
    root.mainloop()
