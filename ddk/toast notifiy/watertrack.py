from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk

# Global variables
water_intake_data = []  # List to store daily water intake data
daily_goal = 100  # Default daily water intake goal (in milliliters)

# Define functions
def submit_intake():
    try:
        intake = float(intake_entry.get())
        water_intake_data.append(intake)
        intake_entry.delete(0, END)  # Clear the intake entry field after submission
        update_progress()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for water intake.")

def set_goal():
    try:
        global daily_goal
        goal = int(goal_entry.get())
        if goal <= 0:
            raise ValueError("Goal must be a positive integer.")
        daily_goal = goal
        update_progress()
        goal_entry.delete(0, END)  # Clear the goal entry field after setting the goal
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def update_progress():
    total_intake = sum(water_intake_data)
    progress = min(total_intake / daily_goal, 1.0)  # Limit the progress to 100%
    progress_bar['value'] = progress * 100
    progress_label.config(text=f"Water Intake Progress: {total_intake:.2f} ml / {daily_goal} ml")

# Window
root = ttk.Window(themename='lumen')
root.title('Water Intake Tracker')
root.geometry('400x300')

# Widget
intake_frame = ttk.Frame(root)
intake_frame.pack(pady=10)

intake_label = ttk.Label(intake_frame, text="Enter Water Intake (ml):")
intake_label.pack(side=LEFT)

intake_entry = ttk.Entry(intake_frame, width=10)
intake_entry.pack(side=LEFT)

submit_button = ttk.Button(intake_frame, text="Submit", command=submit_intake)
submit_button.pack(side=LEFT)

goal_frame = ttk.Frame(root)
goal_frame.pack(pady=10)

goal_label = ttk.Label(goal_frame, text="Set Daily Water Goal (ml):")
goal_label.pack(side=LEFT)

goal_entry = ttk.Entry(goal_frame, width=10)
goal_entry.pack(side=LEFT)

set_goal_button = ttk.Button(goal_frame, text="Set Goal", command=set_goal)
set_goal_button.pack(side=LEFT)

# Progress bar and label
progress_label = ttk.Label(root, text="Water Intake Progress: 0 ml / 100 ml", font=("Arial", 12))
progress_label.pack(pady=20)

progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress_bar.pack()

# Run
root.mainloop()
