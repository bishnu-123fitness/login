from tkinter import *
import tkinter.messagebox as messagebox
import ttkbootstrap as ttk

# Function to show upper body workout details
def show_upper_body_workout():
    upper_body_workout = "Upper Body Workout:\n\n1. Push-ups: 3 sets of 10 reps\n2. Dumbbell Shoulder Press: 3 sets of 8 reps\n3. Bent-over Rows: 3 sets of 10 reps\n4. Bicep Curls: 3 sets of 12 reps"
    messagebox.showinfo("Upper Body Workout", upper_body_workout)

# Function to show lower body workout details
def show_lower_body_workout():
    lower_body_workout = "Lower Body Workout:\n\n1. Squats: 3 sets of 10 reps\n2. Lunges: 3 sets of 8 reps per leg\n3. Deadlifts: 3 sets of 8 reps\n4. Leg Press: 3 sets of 12 reps"
    messagebox.showinfo("Lower Body Workout", lower_body_workout)

# Window
win = ttk.Window(themename='lumen')
win.geometry('550x450')

# Style
my_style = ttk.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 20))
my_style.configure('success.TButton', font=("Helvetica", 12))

# Widgets
upper_button = ttk.Button(win,
                          text='UPPER',
                          style="success.Outline.TButton",
                          width=35,
                          command=show_upper_body_workout)

lower_button = ttk.Button(win,
                          text='LOWER',
                          style="success.Outline.TButton",
                          width=35,
                          command=show_lower_body_workout)

back2_button = ttk.Button(win,
                          text='<<<',
                          style="success.TButton")

# Layouts
upper_button.pack(padx=20, pady=(90, 30))
lower_button.pack(padx=20, pady=(30, 70))

# Run
win.mainloop()
