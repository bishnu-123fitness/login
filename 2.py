from tkinter import*
from tkinter import messagebox
import ast

window=Tk()
window.title('signup')
window.geometry('925x500+300+200')
window.resizable(0,0)

def signup():
    username=user.get()
    password=code.get()
    conform_password=conform_code.get()
    
    
    if password==conform_password:
        try:
         file=open('datasheet.txt','r+')
         d=file.read()
         r=ast.literal_eval(d)
        
        
         dict2={username:password}
         r.update(dict2)
         file.truncate(0)
         file.close()
        
         file=open('datasheet.txt','w')
         w=file.write(str(r))
        
         messagebox.showinfo('signup','sucessfully sign up')
        
        except:
            file=open('datasheet.txt','w')
            pp=str({'username':'password'})
            file.write(pp)
            file.close()
        
    else:
      messagebox.showerror('Invalid','Both password should match')

frame=Frame(window,width=350,height=390,bg='white')
frame.place(x=480,y=50)

heading=Label(frame,text='sign up',font=('microsoft yahei ui light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=="":
        user.insert(0,'username')
        
user=Entry(frame,font=('microsoft yahei ui light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2).place(x=25,y=107)

#########_________________________

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=="":
        code.insert(0,'password')
        
code=Entry(frame,font=('microsoft yahei ui light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2).place(x=25,y=177)


def on_enter(e):
    conform_code.delete(0,'end')
def on_leave(e):
    if conform_code.get()=="":
        conform_code.insert(0,'conform password')
        
conform_code=Entry(frame,font=('microsoft yahei ui light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'conform password')
conform_code.bind("<FocusIn>",on_enter)
conform_code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2).place(x=25,y=247)

Button(frame,text='sign in',cursor='hand2',border=0,command=signup).place(x=35,y=280)
lable=Label(frame,text='I have an account',font=('microsoft yahei ui light',10))
lable.place(x=90,y=340)

signin=Button(frame,text='sign in',cursor='hand2')
signin.place(x=210,y=340)

window.mainloop()