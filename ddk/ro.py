from tkinter import *
from PIL import Image, ImageTk
import sqlite3

def button():
    print('hello ')

def button_2():
    print('2')

def button_3():
    print('3')

def button_4():
    print('4')



root = Tk()
root.title('Dashboard')
root.geometry('400x450')
root.resizable(1,1)
root.config(bg="#ADD8E6")
 
# frame = Frame(root, bg="#ADD8E6", width=400, height=400)
# frame.place(relx=0.5, rely=0.3, anchor=CENTER)

label=Label(root,text='fit your self',bg='black',fg='white')
label.pack(pady=5)

button1= Button(root, text="BMI",bg="black",fg="white",width=100,height=4,command=button)
button1.pack()

button2= Button(root, text="CALORIE",bg="black",fg="white",width=100,height=4,command=button_2)
button2.pack(pady=20)

button3 = Button(root, text="DIET PLAN",bg="black",fg="white",width=100,height=4,command=button_3)
button3.pack(pady=20)

button4= Button(root, text="WORK OUT",bg="black",fg="white",width=100,height=4,command=button_4)
button4.pack()
 
button_5=Button(root,text="<<<<").pack(side=LEFT,padx=10,pady=5)
button_6=Button(root,text=">>>>").pack(side=RIGHT,padx=10)


root.mainloop()