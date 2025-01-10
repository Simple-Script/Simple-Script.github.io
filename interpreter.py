import tkinter as tk
from tkinter import scrolledtext
import re
import webbrowser

class CodeInterpreter:
    def __init__(self):
        # Create main window
        self.window = tk.Tk()
        self.window.title("Code Interpreter")
        self.window.geometry("600x400")
        
        # Create scrolled text area
        self.output = scrolledtext.ScrolledText(self.window, wrap=tk.WORD)
        self.output.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Store variables
        self.variables = {}
        
    def add_text(self, text):
        """Add text to output window"""
        self.output.insert(tk.END, str(text) + "\
")
        self.output.see(tk.END)
        
    def create_link(self, url):
        """Create clickable link"""
        tag = f"link_{len(self.output.tag_names())}"
        self.output.insert(tk.END, f"{url}\
", tag)
        self.output.tag_config(tag, foreground="blue", underline=1)
        self.output.tag_bind(tag, "<Button-1>", lambda e: webbrowser.open(url))
        
    def evaluate_expression(self, expr):
        """Evaluate mathematical expressions"""
        try:
            # Replace variables with their values
            for var, value in self.variables.items():
                expr = expr.replace(var, str(value))
            return eval(expr)
        except:
            return "Error in calculation"
            
    def process_line(self, line):
        """Process each line of the file"""
        line = line.strip()
        if not line:
            return
            
        # Handle text display
        if line.startswith("text("):
            match = re.match(r"text\((.*?)\)", line)
            if match:
                self.add_text(match.group(1))
                return
                
        # Handle links
        if line.startswith("link("):
            match = re.match(r"link\((.*?)\)", line)
            if match:
                self.create_link(match.group(1))
                return
                
        # Handle variable assignment
        if "=" in line and not line.startswith("text("):
            var, value = line.split("=")
            try:
                self.variables[var.strip()] = float(value.strip())
                return
            except ValueError:
                self.add_text(f"Invalid variable assignment: {line}")
                return
                
        # Handle mathematical expressions
        try:
            result = self.evaluate_expression(line)
            self.add_text(f"{line} = {result} ")
        except:
            self.add_text(f"Invalid input: {line} ")
            
    def read_file(self, filepath):
        """Read and process the file"""
        try:
            with open(filepath, 'r') as file:
                self.add_text(f"\
")
                for line in file:
                    self.process_line(line)
        except Exception as e:
            self.add_text(f"Error reading file: {str(e)} ")
            
    def run(self):
        """Start the application"""
        # Read and process the file
        self.read_file("C:\\Users\\Kellarosa\\Desktop\\sample_file.sdl")
        
        # Start the main loop
        self.window.mainloop()

# Create and run the interpreter
interpreter = CodeInterpreter()
interpreter.run()
