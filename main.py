import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()


def setInsDir():
	dirName= filedialog.askdirectory(initialdir="/", title="Select Directory")





canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

setDir = tk.Button(root, text="Set Directory", command=setInsDir)
setDir.pack()

root.mainloop()