from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import time

# defining functions
def clicker():
    show_water_reminder()

def show_water_reminder():
    toast.show_toast()
    root.after(6000, show_water_reminder)  # Repeat the reminder every one hour (3600000 milliseconds)

# window
root = ttk.Window(themename="superhero")
root.title('Water Reminder')
root.geometry('300x200')

# Widget
toast = ToastNotification(title='Water Reminder!',
                          message="It's been 1 hour since you didn't drink water.",
                          duration=3000,  # Display the toast notification for 3 seconds
                          alert=True,
                          position=('sw'))

my_button = ttk.Button(root, text="Reminder button", command=clicker)
my_button.pack(pady=40)

# run
root.mainloop()
