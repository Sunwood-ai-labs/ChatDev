'''
This file contains the Clock class.
'''
from datetime import datetime
class Clock:
    def __init__(self):
        pass
    def get_current_time(self):
        return datetime.now().strftime("%H:%M:%S")