#!/usr/bin/python
#
# Brainfuck Interpreter
# Real
#
# Usage: ./brainfuck.py [FILE]

import sys
import getch
import webbrowser
import os

def execute(filename):
    f = open(filename, "r")
    output = evaluate(f.read())
    f.close()
    open_html(output)

def evaluate(code):
    code = cleanup(list(code))
    bracemap = buildbracemap(code)

    cells, codeptr, cellptr = [0], 0, 0
    output = ""

    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
        if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
        if command == ".":
            output += chr(cells[cellptr])
        if command == ",":
            cells[cellptr] = ord(getch.getch())

        codeptr += 1

    return output

def cleanup(code):
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap

def open_html(output):
    html_content = f"<html><body><pre>{output}</pre></body></html>"
    with open("output.html", "w") as f:
        f.write(html_content)
    webbrowser.open('file://' + os.path.realpath("output.html"))

def main():
    if len(sys.argv) == 2: execute(sys.argv[1])
    else: print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()
