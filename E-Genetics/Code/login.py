from tkinter import * 
from tkinter import messagebox
import hashlib
import os
from Models.User import User
from PIL import ImageTk
from PIL import Image  


  # Designing window for registration
def newScreen(name):
        os.system('python3 paternity.py ' + name)   
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("%dx%d" % (register_screen.winfo_screenwidth(), register_screen.winfo_screenheight()))
    Label(register_screen, text="Welcome In Genetics\n(Registration)", bg="black", fg='red', width="300", height="2", font=("Calibri", 20, 'underline'), pady=50).pack()
   
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="", pady=100).pack()
    username_lable = Label(register_screen, text="Username", font=("Calibri", 17, 'underline'), padx=5)
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, width=50)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password", font=("Calibri", 17, 'underline'), padx=5)
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', width=50)
    password_entry.pack()
    Label(register_screen, text="").pack()
    btn = Button(register_screen, text="Register", width=10, height=1, bg="black", fg='white', command = register_user, font=("Calibri", 17))
    btn.configure(padx=100, pady=20)    
    btn.pack()
# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("%dx%d" % (login_screen.winfo_screenwidth(), login_screen.winfo_screenheight()))
    Label(login_screen, text="Welcome In Genetics\n(Log In)", bg="black", fg='red', width="300", height="2", font=("Calibri", 20, 'underline'), pady=50).pack()
    Label(login_screen, text="", pady=100).pack()
   
    
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username", font=("Calibri", 17, 'underline'), padx=5).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, width=50)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password", font=("Calibri", 17, 'underline'), padx=5).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', width=50)
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    btn = Button(login_screen, text="Login", width=10, height=1, command = login_verify, bg='black', fg='white', font=("Calibri", 17))
    btn.configure(padx=100, pady=20)    
    btn.pack()
   
# Implementing event on register button
user = User()
    
def register_user():
    username_info = username.get()
    password_info = password.get()
    hashed_password = hashlib.sha256(password_info.encode('utf-8')).hexdigest()
    if(username_info == '' or password_info == ''):
        messagebox.showerror('Error', 'Error: Please Fill all Requirements')
    else:
     if(user.Registration(username_info, hashed_password)):
        messagebox.showerror('Error', 'Error: Please Try another user Name or another password')        
     else:
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            register_screen.destroy()
        
# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    hashed_password1 = hashlib.sha256(password1.encode('utf-8')).hexdigest()
    if(user.logIn(username1, hashed_password1)):
        main_screen.destroy()
        newScreen(username1)
        
    else:
        messagebox.showerror('Error', 'Error: Data Is Not Exist')   
    

# Designing popup for login success


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 



# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("%dx%d" % (main_screen.winfo_screenwidth(), main_screen.winfo_screenheight()))
    main_screen.title("Account Login")
    Label(text="Welcome In Genetics", bg="black", fg='red', width="300", height="2", font=("Calibri", 20, 'underline'), pady=50).pack()
    Label(text="").pack()
    load = Image.open("Images/family-law.png")
    render = ImageTk.PhotoImage(load) 
    img = Label(image=render)
    img.image = render
    img.place(x=700, y=200)
  
    Button(text="Login", height="2", width="30", command = login, background='darkred',fg='white').place(x=840, y=700)
    Button(text="Register", height="2", width="30", command=register, background='darkgreen',fg='white').place(x=840, y=800)

    main_screen.mainloop()


main_account_screen()
