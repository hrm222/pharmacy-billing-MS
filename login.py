from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk


def sign_up():

    

    win.destroy()

    
    win2= Tk()

    win2.config(bg="#072028") 
    win2.geometry("700x500+280+50")
    win2.title("sign up")
    win2.resizable(False,False)

    frame2 = Frame(win2,bg="#0B2f3A")
    frame2.pack(padx=20,pady=15,fill="both",expand=True)

    titelLbl = Label(frame2,text="Creat A New Account",bg="#0B2f3A",fg="white")
    titelLbl.grid(row=0,column=0,columnspan=2,padx=15,pady=10)

    first_name_lbl = Label(frame2,text="First name",bg="#0B2f3A",fg="white")
    first_name_lbl.grid(row=1,column=0,padx=15,pady=10)
    first_name_entry =Entry(frame2)
    first_name_entry.grid(row=1,column=1)

    
    last_name_lbl = Label(frame2,text="last name",bg="#0B2f3A",fg="white")
    last_name_lbl.grid(row=2,column=0,padx=15,pady=10)
    last_name_entry =Entry(frame2)
    last_name_entry.grid(row=2,column=1)

    email_lbl = Label(frame2,text="Email",bg="#0B2f3A",fg="white")
    email_lbl.grid(row=3,column=0,padx=15,pady=10)
    email_entry =Entry(frame2)
    email_entry.grid(row=3,column=1)

    password_lbl = Label(frame2,text="Password",bg="#0B2f3A",fg="white")
    password_lbl.grid(row=4,column=0,padx=15,pady=10)
    password_entry =Entry(frame2)
    password_entry.grid(row=4,column=1)

    conf_password_lbl = Label(frame2,text="confirm Password",bg="#0B2f3A",fg="white")
    conf_password_lbl.grid(row=5,column=0,padx=15,pady=10)
    conf_password_entry =Entry(frame2)
    conf_password_entry.grid(row=5,column=1)

    sign_img = Image.open("he4.png")
    sign_photo =ImageTk.PhotoImage(sign_img)
    imgLable =Label(frame2,width=600,height=500,bg="red",image=sign_photo)
    imgLable.place(x=300)

    sign_img2= Image.open("he5.jpeg")
    sign_photo2 = ImageTk.PhotoImage(sign_img2)
    imgLable2 =Label(frame2,width=296,height=168,image=sign_photo2,bg="#0B2f3A")
    imgLable2.place(y=304)
    
   
        

    

    def save():
        
        conn = None
        try:
            Fname = first_name_entry.get()
            Lname = last_name_entry.get()
            email = email_entry.get()
            
            flag =False
            if password_entry.get()==conf_password_entry.get():
                flag=True
            if flag:
                 passw = password_entry.get()
            else:
                messagebox.showwarning(title="Warning",message="passwords does not match")
                


            conn = sqlite3.connect('accountsDB.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO account VALUES(?,?,?,?)',[Fname,Lname,email,passw])
            conn.commit()
            conn.close()
            first_name_entry.delete(0,END)
            last_name_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)
            conf_password_entry.delete(0,END)



        except:
            print("Erorr")
       

    btn3 = Button(frame2,
                  text="Sign Up",
                  fg="white",
                  bg="#DBA901",
                  command=save,activeforeground="white",activebackground="#DBA901")
    btn3.grid(row=6,column=0,columnspan=2)
    
    btn3 = Button(frame2,
                  text="Go Back",
                  fg="white",
                  bg="#DBA901",
                  activeforeground="white",activebackground="#DBA901")
    btn3.grid(row=6,column=1,columnspan=2)
    

    mainloop()

    




win=Tk()
menubar = Menu(win)
win.config(menu=menubar)
icon = PhotoImage(file='hospital_icon.png')

'''admin = Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=admin)
admin.add_command(label="Save")
admin.add_command(label="Exit",command=quit)'''
def system():
    import main
    pass

admin = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Admin portal",menu=admin)
admin.add_command(label="Login")
admin.add_command(label="employees")
admin.add_command(label="System",command=system)

win.geometry("800x500+280+50")
win.title("Login")
win.config(bg="#072028")
win.iconphoto(True,icon)
win.resizable(False,False)



frame = Frame(win,bg="#0B2f3A",bd=10)
frame.pack(padx=60,pady=20,fill="both",expand=True)

lable = Label(frame,text="Login system",background="#0B2f3A",font=("Arial",20),fg="white")
lable.pack(padx=10,pady=12)

user_lbl = Label(frame,text="User Name",bg="#0B2f3A",fg="white")
user_lbl.pack(padx=10)

user_entry = Entry(frame)
user_entry.pack(padx=10,pady=12)

pass_lbl = Label(frame,text="Password",bg="#0B2f3A",fg="white")
pass_lbl.pack(padx=10)

pass_entry = Entry(frame,show="*")
pass_entry.pack(padx=10,pady=12)

conn2 =sqlite3.connect('accountsDB.db')
cur2 =conn2.cursor()

cur2.execute('SELECT Eamil,password FROM account')
emails = cur2.fetchall()

def login():
    flag=False
    for rows in emails:
        if user_entry.get() == rows[0] and pass_entry.get() == str(rows[1]) :
            flag=True 
    if flag:
        
        messagebox.showinfo(title="valid",message="valid user")
        win.destroy()
        import main
        pass
        
    else:
        messagebox.showerror(title="Error",message="Invalid user")
    
        conn2.close()
def display():
    for i in emails:
        print(i[1])



conn2.close()




btn = Button(frame,
             text="Login",
             command=login,
             background="#DBA901",
             fg="white",activeforeground="white",activebackground="#DBA901")
btn.pack(padx=10)

btn2 = Button(frame,
              text="Creat new Account",
              command=sign_up,
              background="#DBA901",
              fg="white",activeforeground="white",activebackground="#DBA901")
btn2.pack(padx=30,pady=10)



img2 = Image.open("pharmacy2.png")
photo2 = ImageTk.PhotoImage(img2)



lb = Label(frame,image=photo2,bg="#0B2f3A")
lb.place(x=0,y=260,height=350)

def Admin_login():
    pass

def employees():
    pass


win.mainloop