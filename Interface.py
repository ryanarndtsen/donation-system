from UserClass import *
from database import *
from tkinter import *

person = User()
def defineAttributes():
    global e
    global f
    global g
    string = e.get()
    string2 = f.get()
    string3 = g.get()
    person.firstName = string
    person.lastName = string2
    person.setPassword(string3)
    print(person.getName())
    print(person.password)

temp = User()
def findPassword():
    stri= e.get()
    stri2 = f.get()
    temp.setName(stri,stri2)
 #   temp. #when database is figured out make this method a search which will find and print password of a certain name
    
root = Tk()

title = Label(root, text = "Donation System", fg = "blue", bg = "red")
title.grid(row = 0, column = 1)
label1 = Label(root, text = "First Name")
label2 = Label(root, text = "Last Name")
label3 = Label(root, text = "Password")
label1.grid(row = 1, sticky = E)
label2.grid(row = 2, sticky = E)
label3.grid(row = 3, sticky = E)

e = Entry(root)
f = Entry(root)
g = Entry(root)
e.grid(row = 1, column = 1)
f.grid(row = 2, column = 1)
g.grid(row = 3, column = 1)

c = Checkbutton(root, text="Keep me logged in.")
c.grid(row = 4, column = 1)

button1 = Button(root, text = "Log In", bg ="blue", fg = "blue", command = defineAttributes)
button1.grid(row = 5, column = 3)

button2 = Button(root, text = "Forgot Password", bg = "blue",fg = "blue")
button2.grid(row = 6, column = 3)
root.mainloop()

