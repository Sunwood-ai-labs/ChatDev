import tkinter as tk
from clock import Clock
# Create a tkinter window
window = tk.Tk()
window.title("Simple Clock")
# Create a label to display the time
time_label = tk.Label(window, font=("Arial", 80))
# Update the time every second
def update_time():
    current_time = clock.get_current_time()
    time_label.config(text=current_time)
    time_label.after(1000, update_time)
# Create an instance of the Clock class
clock = Clock()
# Start updating the time
update_time()
# Pack the label into the window
time_label.pack()
# Start the tkinter event loop
window.mainloop()