from tkinter import*
import ttkbootstrap as ttk


# window 
win = ttk.Window(themename='lumen')
win.geometry('550x450')

# /// style /// 
my_style = ttk.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 20))
my_style.configure('success.TButton', font=("Helvetica", 12))

# Widgets 
upper_button = ttk.Button(win,
                        text='UPPER',
                        style="success.Outline.TButton",
                         width=35)

lower_button = ttk.Button(win,
                        text='LOWER',
                        style="success.Outline.TButton",
                         width=35)

back2_button = ttk.Button(win,
                         text='<<<',
                         style="success.TButton"
                         )

# layouts 
upper_button.pack(padx=20, pady=(90,30))
lower_button.pack(padx=20, pady=(30,70))


# run
win.mainloop()