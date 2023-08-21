from tkinter import*
from tkinter import Entry
from tkinter import messagebox
from PIL import ImageTk
def login():
    if usernameentry.get()=='' or passwordentry.get=='':
        messagebox.showerror('Error','Fields cannot  be empty')
    elif usernameentry.get()=='aravind' and passwordentry.get()=='333':
          messagebox.showinfo('SUCCESS','Login Succesfull')
          window.destroy()
          import SMS


    else:
        messagebox.showerror('Error','Invalid credentials! Please enter valid credentials')

    print("")
window=Tk()
window.geometry('1800x800+0+0')
window.title('LOGIN SYSTEM OF STUDENT MANAGEMENT SYSTEM')
background=ImageTk.PhotoImage(file='b2.jpg')
blabel=Label(window,image=background)
blabel.place(x=0,y=0)
Loginframe=Frame(window,bg='#2596be')
Loginframe.place(x=600,y=250)
logoimage=PhotoImage(file='graduates.png')
logolabel=Label(Loginframe,image=logoimage,bg='#2596be')
logolabel.grid(row=0,column=0,columnspan=2,pady=10)
usimage=PhotoImage(file='user.png')
usernameLabel=Label(Loginframe,image=usimage,text="USERNAME",compound=LEFT,font=('times new roman',16,'bold'),bg='#2596be')
usernameLabel.grid(row=1,column=0,pady=10)
usernameentry=Entry(Loginframe,font=('times new roman',16,'bold'),bd=5)
usernameentry.grid(row=1,column=1,pady=10,padx=10)
psimage=PhotoImage(file='password.png')
passwordLabel=Label(Loginframe,image=psimage,text="PASSWORD",compound=LEFT,font=('times new roman',16,'bold'),bg='#2596be')
passwordLabel.grid(row=2,column=0,pady=10)
passwordentry=Entry(Loginframe,font=('times new roman',16,'bold'),bd=5)
passwordentry.grid(row=2,column=1,pady=10)
logicbutton=Button(Loginframe,text='LOGIN',font=('times new roman',14,'bold'),bg='#30b497',width=8,fg="white",activebackground='#30b497',
                   activeforeground='#30b497',cursor='hand2',command=login)
logicbutton.grid(row=3,column=1)





window.mainloop()