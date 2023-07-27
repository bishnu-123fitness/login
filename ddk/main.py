import tkinter as tk
import ttkbootstrap as ttk


# /// window /// 
window = ttk.Window(themename='lumen')
window.title('Hastag Fitness')
window.geometry('550x450')
window.minsize(550,450)

# /// style /// 
my_style = ttk.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 20))
my_style.configure('success.TButton', font=("Helvetica", 12))



# widgets 
main_frame = ttk.Frame(window, width=530, height=420)
main_frame.pack(pady=30)


# /// main buttons /// 

BMI_button = ttk.Button(main_frame, text='BMI',
                        style="success.Outline.TButton",
                          width=40)
calorie_button = ttk.Button(main_frame,
                            text='CALORIE COUNT',
                            style="success.Outline.TButton",
                             width=40)
diet_button = ttk.Button(main_frame,
                            text='DIET PLAN',
                            style="success.Outline.TButton",
                             width=40)
workout_button = ttk.Button(main_frame,
                            text='WORKOUT',
                            style="success.Outline.TButton",
                             width=40)

back_button = ttk.Button(main_frame,
                         text='<<<',
                         style="success.TButton"
                         )

# widgets layout 
BMI_button.pack(padx=10, pady=15)
calorie_button.pack(padx=10, pady= 15)
diet_button.pack(padx=10, pady= 15)
workout_button.pack(padx=10, pady= 15)
back_button.pack(pady=15)




# run 
window.mainloop()