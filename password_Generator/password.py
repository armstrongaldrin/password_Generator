import tkinter 
from tkinter import *
from tkinter import messagebox as box
import secrets
import string
import pyperclip

def genrate_password(lenght, uppercase ,numbers, special):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation
    if not characters:
        box.showerror("Error","No character set selected!")

    password = ''.join(secrets.choice(characters) for i in range(lenght) )
    #password_entry.delete(0,window.destroy)
    password_entry.insert(0,password)

def clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    box.showinfo("Cpoied","Password copied to clipboard!")

window = Tk()
window.title("Password Generator")

l1 = Label(window,text="Password Length:")
l1.place(x=100,y=20)
length_spinbox = Spinbox(window,from_=8, to_=32, width=5, )

length_spinbox.place(x=230,y=20)


uppercase_var = BooleanVar()
Checkbutton(window,text="Include Uppercase Letters", variable=uppercase_var).place(x=100,y=40)

numbers_var = BooleanVar()
Checkbutton(window, text="Include Numbers", variable=numbers_var).place(x=100,y=60)

special_var = BooleanVar()
Checkbutton(window,text="Include Special Characters", variable=special_var).place(x=100,y=80)


b1 = Button(window,text="Generate Password",command=lambda: genrate_password(int(length_spinbox.get()), uppercase_var.get(),numbers_var.get(), special_var.get()))
b1.place(x=150,y=110)

l2 = Label(window,text="Generated Password:")
l2.place(x=100,y=150)

password_entry = Entry(window, width=30)
password_entry.place(x=100,y=170)

copy_button = Button(window,text="Copy to Clipboard",command=clipboard)
copy_button.place(x=100,y=200)












window.geometry("400x400")
window.mainloop()
