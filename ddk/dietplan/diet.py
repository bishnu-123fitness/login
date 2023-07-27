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
gain_button = ttk.Button(win,
                        text='WEIGHT GAIN',
                        style="success.Outline.TButton",
                         width=35)

loss_button = ttk.Button(win,
                        text='WEIGHT LOSS',
                        style="success.Outline.TButton",
                         width=35)

back1_button = ttk.Button(win,
                         text='<<<',
                         style="success.TButton"
                         )

# layouts 
gain_button.pack(padx=20, pady=(90,30))
loss_button.pack(padx=20, pady=(30,70))
back1_button.pack(pady=20)


# run
win.mainloop()