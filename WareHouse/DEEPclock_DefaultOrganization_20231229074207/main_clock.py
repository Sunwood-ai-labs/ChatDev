import tkinter as tk
from time import strftime
from time_label import TimeLabel
class MainClock:
    def __init__(self, root):
        self.root = root
        self.time_label = TimeLabel(root)
        self.update_time()
    def update_time(self):
        current_time = strftime('%H:%M:%S')
        self.time_label.set_time(current_time)
        self.root.after(1000, self.update_time)   # Pass 'self' as an argument
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.main_clock = MainClock(self.root)
    def start(self):
        self.root.mainloop()