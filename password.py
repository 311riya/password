from tkinter import*
import string
import random
from tkinter import messagebox
import re
import sqlite3

with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
cursor.execute("SELECT * FROM users")
db.commit()
db.close()



def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation


    all= small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    
    password=random.sample(all,password_length)
    passwordField.insert(0,password)

def accept():   
    with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            find_user = ("SELECT * FROM users WHERE Username = ?")
            cursor.execute(find_user, [(passwordField1.get())])

            if cursor.fetchall():
            	messagebox.showerror("This username already exists!", "Please use an another username")
            else:
            	insert = str("INSERT INTO users(Username, GeneratedPassword) VALUES(\'%s\', \'%s\');"%(passwordField1.get(), length_Box.get()))
            	cursor.execute(insert)
            	db.commit()
            	messagebox.showinfo("Success!", "Password generated successfully")

 
def reset():
     passwordField1.delete(0,END)
     length_Box.delete(0,END)
     passwordField.delete(0,END)


root=Tk()
root.config()
root.geometry('660x500')

Font=('times new roman',13)
passwordLabel=Label(root,text='Password Generator',anchor=N, fg='darkblue', font='arial 20 bold')
passwordLabel.grid(row=0,column=1)


lengthLabel=Label(root,text='Enter user name:',font=Font,fg='black',pady=7)
lengthLabel.grid(row=1,column=0)


passwordField1=Entry(root,width=27,bd=3)
passwordField1.grid(row=1,column=1)


lengthLabel=Label(root,text='Password Length:',font=Font,fg='black',pady=7)
lengthLabel.grid(row=2,column=0)


length_Box=Spinbox(root,from_=5,to_=18,width=16,font=Font,fg='black')
length_Box.grid(row=2,column=1)


lengthLabel=Label(root,text='Generate password:',font=Font,fg='black',pady=5)
lengthLabel.grid(row=3,column=0)


passwordField=Entry(root,width=27,bd=3)
passwordField.grid(row=3,column=1)

blank_label5 = Label(text="")
blank_label5.grid(row=4, column=0)

generateButton=Button(root,text='Generate Password',font=('times new roman',13,'bold'),command=generator, fg='white', bg='darkblue',padx=1, pady=1)
generateButton.grid(row=5,column=1)


blank_label5 = Label(text="")
blank_label5.grid(row=6, column=0)

AcceptButton=Button(root,text='Accept',font=Font,padx=1, pady=1,command=accept)
AcceptButton.grid(row=7,column=1)

blank_label5 = Label(text="")
blank_label5.grid(row=8, column=0)

ResetButton=Button(root,text='Reset',font=Font,padx=1, pady=1,command=reset)
ResetButton.grid(row=9,column=1)




root.mainloop()
