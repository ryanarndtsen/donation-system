from UserClass import *
from database import *
from tkinter import *
from tkinter.font import Font
#from Interface import *

class LogInPage(Frame):
    def __init__(self, master):
        myFont = Font(root, family="Times New Roman", size=20, underline=1, weight="normal")
        self.frame = Frame(master)
        self.frame.pack()

        self.title1 = Label(self.frame, text = "Donation System", fg = "white", bg = "black")
        self.title1.configure(font=myFont)
        self.title1.grid(row = 0, column = 1)

        self.label5 = Label(self.frame, text = "First Name")
        self.label6 = Label(self.frame, text = "Last Name")
        self.label7 = Label(self.frame, text = "Password")
        self.label5.grid(row=1, sticky=E)
        self.label6.grid(row=2, sticky=E)
        self.label7.grid(row=3, sticky = E)

        self.z = Entry(root)
        self.y = Entry(root)
        self.x = Entry(root)
        self.z.grid(row=1, column=1)
        self.y.grid(row=2, column=1)
        self.x.grid(row=3, column=1)


root = Tk()
app = LogInPage(root)
root.mainloop()