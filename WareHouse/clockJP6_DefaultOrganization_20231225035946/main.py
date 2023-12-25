from tkinter import *
'''
This is the main script that creates the application window and initializes the clock.
'''
import tkinter as tk
from clock import Clock
if __name__ == "__main__":
    root = tk.Tk()
    clock = Clock(root)
    root.mainloop()
    root.destroy()