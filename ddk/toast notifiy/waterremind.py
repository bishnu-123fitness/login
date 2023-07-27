from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import time

# defining functions
def clicker():
    show_water_reminder()

def show_water_reminder():
    toast.show_toast()
    root.after(reminder_interval * 60 * 1000, show_water_reminder)  # Convert minutes to milliseconds and repeat the reminder

def set_reminder_interval():
    global reminder_interval
    try:
        interval = int(interval_entry.get())
        if interval <= 0:
            raise ValueError("Interval must be a positive integer.")
        reminder_interval = interval
        interval_label.config(text=f"Reminder Interval: {reminder_interval} minutes")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# window
root = ttk.Window(themename="superhero")
root.title('Water Reminder')
root.geometry('300x250')

# Widget
toast = ToastNotification(title='Stay Hydrated!',
                          message="Remember to take a break and drink some water.",
                          duration=3000,  # Display the toast notification for 3 seconds
                          alert=True,
                          position=('sw'))

my_button = ttk.Button(root, text="Start Reminder", command=clicker)
my_button.pack(pady=10)

interval_frame = ttk.Frame(root)
interval_frame.pack(pady=10)

interval_label = ttk.Label(interval_frame, text="Reminder Interval: 60 minutes")
interval_label.pack(side=LEFT)

interval_entry = ttk.Entry(interval_frame, width=5)
interval_entry.pack(side=LEFT)

set_interval_button = ttk.Button(interval_frame, text="Set Interval", command=set_reminder_interval)
set_interval_button.pack(side=LEFT)

# Initialize the reminder interval to 60 minutes (1 hour)
reminder_interval = 60

# run
root.mainloop()
