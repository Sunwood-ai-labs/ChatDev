'''
This module contains the Clock class that displays the current time in Japanese.
'''
import tkinter as tk
import time
class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Japanese Clock")
        self.label = tk.Label(root, font=("Arial", 80), bg="white")
        self.label.pack(fill=tk.BOTH, expand=True)
        self.update_clock()
    def update_clock(self):
        '''
        Updates the clock label with the current time every second.
        '''
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)