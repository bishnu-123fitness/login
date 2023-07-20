from tkinter import*
from tkinter import messagebox
from PIL import  ImageTk,Image
import ast

root=Tk()
root.title ("login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(0,0)

img=ImageTk.PhotoImage(Image.open("a.png"))
Label(root,image=img,bg="white").place(x=-55,y=50)
    
  
def signup_command():
    window=Toplevel(root)  
    
    window.title('Signup')
    window.geometry('925x500+300+200')
    window.configure(bg="#fff")
    window.resizable(0,0)

    
    def signup():
        Username=user.get()
        Password=code.get()
        conform_password=conform_code.get()
    
        if Password==conform_password:
            try:
                 file=open('datasheet.txt','r+')
                 d=file.read()
                 r=ast.literal_eval(d)
        
        
                 dict2={Username:Password}
                 r.update(dict2)
                 file.truncate(0)
                 file.close()
        
                 file=open('datasheet.txt','w')
                 w=file.write(str(r))
        
                 messagebox.showinfo('signup','sucessfully sign up')
                 window.destroy()
        
            except:
                 file=open('datasheet.txt','w')
                 pp=str({'Username':'Password'})
                 file.write(pp)
                 file.close()
        
        else:
            messagebox.showerror('Invalid','Both password should match')
    def sign():
        window.destroy()

    
    img=ImageTk.PhotoImage(Image.open("b.png"))
    Label(window,image=img,bg="white").place(x=10,y=50)
    
    frame=Frame(window,width=350,height=390,bg='white')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Sign up',font=('microsoft yahei ui light',23,'bold'))
    heading.place(x=100,y=5)

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=="":
            user.insert(0,'username')
        
    user=Entry(frame,width=25,fg="black",border=0,bg="white",font=('microsoft yahei ui light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2).place(x=25,y=107)


    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=="":
            code.insert(0,'password')
        
    code=Entry(frame,width=25,fg="black",border=0,font=('microsoft yahei ui light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2).place(x=25,y=177)


    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=="":
            conform_code.insert(0,'conform password')
        
    conform_code=Entry(frame,width=25,fg="black",border=0,font=('microsoft yahei ui light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0,'Conform Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2).place(x=25,y=247)

    Button(frame,width=39,pady=7,text='Sign up',bg="#57a1f8",fg="white",border=0,command=signup).place(x=35,y=280)
    lable=Label(frame,text='I have an account',fg="black",bg="white",font=('microsoft yahei ui light',10))
    lable.place(x=90,y=340)

    signin=Button(frame,width=6,text='Sign in',border=0,bg="white",cursor="hand2",fg="#57a1f8",command=sign)
    signin.place(x=210,y=340)

    window.mainloop()
 
 
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=510,y=70)

heading=Label(frame,text="Sign in",fg='black',bg="white",font=('microsoft yahei ui light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete (0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert (0,'username')
        
        

user =Entry(frame,width=25,border=0)
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete (0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert (0,'Password')
        
        
code =Entry(frame,width=25,border=0)
code.place(x=30,y=150)
code.insert(0,'password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

def signin():
    username=user.get()
    password=code.get()
    
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
 
    
    if username in r.keys()and password==r[username]:
        root2=Toplevel(root)
        root2.title("Fitness app")
        root2.geometry("500x500")
        root2.config(bg="white")
        
        welcome_message=" welcome to the fitness center "
        Label(root2,text=welcome_message,bg="#fff",font=("Calibary Body",10,"bold")).place(x=110,y=240)
        
    else:
        messagebox.showerror("Invalid","Invalid username or password")
    root2.mainloop()        

        


Button(frame,width=39,text='Sign in',command=signin).place(x=35,y=204)
label=Label(frame,text="Dont have an account?",border=0)
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,cursor='hand2',command=signup_command)
sign_up.place(x=215,y=270)

root.mainloop()