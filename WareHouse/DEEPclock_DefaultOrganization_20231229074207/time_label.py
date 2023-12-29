from tkinter import Label
import time
class TimeLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def set_time(self, current_time):
        self.config(text=current_time)