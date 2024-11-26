import tkinter as tk

class CrosshairApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        self.root.geometry("15x15+0+0")
        self.canvas = tk.Canvas(self.root, width=15, height=15, bg='green', highlightthickness=0)
        self.canvas.pack()
        self.draw_crosshair()
        self.center_crosshair()
        self.root.mainloop()

    def draw_crosshair(self):
        self.canvas.create_line(0, 0, 0, 0, fill='green', width=1)
        self.canvas.create_line(0, 0, 0, 0, fill='green', width=1)

    def center_crosshair(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - 50
        y = (screen_height // 2) - 50
        self.root.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CrosshairApp(root)
