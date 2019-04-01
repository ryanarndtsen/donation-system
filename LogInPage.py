from UserClass import *
from database import *
from tkinter import *
from tkinter.font import Font
#from Interface import *
from HomePage import GiverHomePage, HoboHomePage

class LogInPage(Frame):
    def __init__(self, master):
        myFont = Font(master, family="Times New Roman", size=20, underline=1, weight="normal")
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
            u = User() #make a temp user for easier class interaction later
            u.setName(self.z.get(),self.y.get())
            try:
                temp = str(read_record(u.getName())[2])
            except:
                print("Account name does not exist.")
            try:
                u.setPassword(temp) #returning NoneType when name is not in database
                if (u.getPassword() == self.x.get()):
                    print("Log In successful.")
                    list = read_record(u.getName())
                    print(str(list[5]))
                    if str(list[5]) == "Giver":
                        giver = Giver(u.firstName, u.lastName, list[1], [0,0,0,0], list[2], list[3], list[4])
                        self.changePageGiver(giver)
                    elif str(list[5]) == "Hobo":
                        hobo = Hobo(u.firstName, u.lastName, list[1], [0,0,0,0], list[2], list[3], list[4])
                        self.changePageHobo(hobo)
                    else:
                        print("WTF")
                else:
                    print("Invalid password.")
            except:
                print("Please re-enter information.")
    def changePageGiver(self, giver):
        root.destroy()
        root2 = Tk()
        app = GiverHomePage(root2, giver)
        root2.mainloop()
    def changePageHobo(self, hobo):
        root.destroy()
        root2 = Tk()
        app = HoboHomePage(root2, hobo)
        root2.mainloop() #fix

root = Tk()
app = LogInPage(root)
root.mainloop()
