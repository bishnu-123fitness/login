from tkinter import*
from PIL import  ImageTk,Image
from tkinter import messagebox

def signup():
    pass

root=Tk()
root.title("login")
root.resizable(0,0)
root.geometry("900x600")
root.iconbitmap("g.ico")
img=ImageTk.PhotoImage(Image.open("a.png"))
Label(root,image=img).place(x=5,y=50)

def signin():
    entered_username=username.get()
    entered_password=password.get()
    
    if entered_username=="bishnu"and entered_password=="12345":
        messagebox.showinfo("login","login successful")
        
    else:
        messagebox.showinfo("login","Invalid username or password.")
        
     
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=600,y=100)


Label(frame, text="Username").place(x=50, y=70,)
username = Entry(frame)
username.place(x=115, y=70)

Label(frame, text="Password").place(x=50, y=110)
password = Entry(frame, show="*")
password.place(x=115, y=110)

topic=Label(frame,text="Sign in",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI light",23,"bold"))
topic.place(x=110,y=5)

mybutton=Button(frame,text="forgotpassword")
mybutton.place(x=110,y=210)

account=Label(frame,text="Dont have account?")
account.place(x=5,y=270)
# def open_signup_window():
#     signup_window = Toplevel(root)
#     signup_window.title("Registration")
#     signup_window.resizable(0, 0)
#     signup_window.geometry("800x480")
#     signup_window.iconbitmap("h.ico")


# # def signup():
# #     entered_username = username.get()
# #     entered_password = password.get()

# #     print("Username:", entered_username)
# #     print("Password:", entered_password)
    
# #     if entered_username==" "and entered_password==" ":
# #         messagebox.askokcancel(title="sucess",Message="suser have login sucessfully")
        
# #     img1=ImageTk.PhotoImage(Image.open("b.png"))
# #     Label(root,image=img1).place(x=5,y=50)
    
# frame = Frame(root, width=290, height=300, bg="white")
# frame.place(x=500, y=100)

# email_label = Label(frame, text="Email")
# email_label.place(x=50, y=50)
# email_entry = Entry(frame)
# email_entry.place(x=110, y=50)

# username_label = Label(frame, text="Username")
# username_label.place(x=50, y=80)
# username = Entry(frame)
# username.place(x=110, y=80)

# password_label = Label(frame, text="Password")
# password_label.place(x=50, y=115)
# password = Entry(frame, show="*")
# password.place(x=110, y=115)

# confirm_password = Label(frame, text="Confirm Password")
# confirm_password.place(x=10, y=160)
# confirm_password = Entry(frame, show="*")
# confirm_password.place(x=120, y=160)

# topic = Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI light", 18, "bold"))
# topic.place(x=110, y=5)

# mybutton = Button(frame, text="Sign in")
# mybutton.place(x=20, y=200)

# windows = Label(frame, text="Sign up", cursor="hand2", fg="blue")
# windows.place(x=215, y=270)
# windows.bind("<Button-1>", lambda event: open_signup_window())

# mybutton = Button(frame, text="Login", font=("Microsoft YaHei UI light", 13, "bold"), command=signin)
# mybutton.place(x=40, y=150)

root.mainloop()
