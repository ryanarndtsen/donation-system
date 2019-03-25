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

        self.z = Entry(self.frame)
        self.y = Entry(self.frame)
        self.x = Entry(self.frame)
        self.z.grid(row=1, column=1)
        self.y.grid(row=2, column=1)
        self.x.grid(row=3, column=1)

        self.liButton = Button(self.frame, text = "Log In", command = self.liButtonFunc)
        self.liButton.grid(row=4, column = 2)

    def liButtonFunc(self):
        if self.z.get() == "" or self.y.get() == "" or self.x.get() == "":
            print("First name, last name, and password need to be defined.")
        else:
            name = self.z.get() + " " + self.y.get()
            try:
                passw = str(read_record(name)[2]) #returning NoneType when name is not in database
                if (passw == self.x.get()):
                    print("Log In successful.")
                    # move to home page
                else:
                    print("Invalid password.")
            except:
                print("Account name does not exist.")

root = Tk()
app = LogInPage(root)
root.mainloop()
