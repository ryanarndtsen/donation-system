from UserClass import *
from database import *
from tkinter import *
from tkinter.font import Font

person = User()
def defineAttributes():
    global e
    global f
    global g
    global h
    string = e.get()
    string2 = f.get()
    string3 = g.get()
    string4 = h.get()
    person.firstName = string
    person.lastName = string2
    person.setAge(string3)
    person.setPassword(string4)
    name = person.getName()
    age = person.getAge()
    passw = person.getPassword()
    write_record(name, age, passw)
def button1_func():
    if e.get() == "" or f.get() == "" or g.get() == "":
        print("First, last name, and age need to be defined.")
    try:
        int(g.get())
    except:
        print("Age must be a number.")
    else:
        passw = h.get()
        if hasCapitals(passw) and hasNumbers(passw) and len(passw) >= 6:
            defineAttributes()
        else:
            print("Invalid password.")

root = Tk()
myFont = Font(root, family = "Times New Roman", size = 20, underline = 1, weight = "normal")
title = Label(root, text = "Donation System", fg = "white", bg = "black")
title.configure(font = myFont)
title.grid(row = 0, column = 1)
label1 = Label(root, text = "First Name")
label2 = Label(root, text = "Last Name")
label3 = Label(root, text = "Age")
label4 = Label(root, text = "Password")
label1.grid(row = 1, sticky = E)
label2.grid(row = 2, sticky = E)
label3.grid(row = 3, sticky = E)
label4.grid(row = 4, sticky = E)

e = Entry(root)
f = Entry(root)
g = Entry(root)
h = Entry(root)
e.grid(row = 1, column = 1)
f.grid(row = 2, column = 1)
g.grid(row = 3, column = 1)
h.grid(row = 4, column = 1)

c = Checkbutton(root, text="Keep me logged in.")
c.grid(row = 5, column = 1)

button1 = Button(root, text = "Create Account", bg ="blue", fg = "blue", command = button1_func)
button1.grid(row = 6, column = 3)

root.mainloop()
#need to get program to switch to next window (classes???)
