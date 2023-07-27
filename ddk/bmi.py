import tkinter as tk
import ttkbootstrap as ttk


window = ttk.Window()
window.geometry('600x500')


menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)
 
# main place layout 
menu_frame.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)


menu_button1 = ttk.Button(menu_frame, text = 'Button 1')
menu_button2 = ttk.Button(menu_frame, text = 'Button 2')
menu_button3 = ttk.Button(menu_frame, text = 'Button 3')


menu_button1.grid(row = 0, column = 0, sticky = 'nswe', columnspan = 2, padx = 4, pady = 4)
menu_button2.grid(row = 0, column = 2, sticky = 'nswe', padx = 4, pady = 4)
menu_button3.grid(row = 1, column = 0,rowspan=3, columnspan = 3, sticky = 'nsew', padx = 4, pady = 4)

# run 
window.mainloop()