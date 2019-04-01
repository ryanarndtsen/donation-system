from UserClass import *
from database import *
from tkinter import *
from tkinter.font import Font

class GiverHomePage(Frame):
    def __init__(self,master, Giver):
        myFont = Font(master, family="Times New Roman", size=20, underline=1, weight="normal")
        myFont2 = Font(master, family="Times New Roman", size = 18)
        self.frame = Frame(master)
        self.frame.pack()

        self.title1 = Label(self.frame, text="Donation System", fg="white", bg="black")
        self.title1.configure(font=myFont)
        self.title1.grid(row=0, column=1)

        s1 = "{}(GIVER)".format(Giver.getName())
        self.labela = Label(self.frame, text = s1)
        self.labela.configure(font = myFont2)
        self.labela.grid(row=1, column = 1)

        self.labelb = Label(self.frame, text = "Funds:")
        self.labelb.grid(row=2, sticky = E)
        self.labelc = Label(self.frame, text = "Total Given:")
        self.labelc.grid(row=3, sticky = E)
        self.labeld = Label(self.frame, text = "Rewards:")
        self.labeld.grid(row=4, sticky = E)

        funds = "${}".format(Giver.getFunds())
        totalGiven = "${}".format(Giver.gettG())
        rewards =', '.join(Giver.checkRewards())
        self.labele = Label(self.frame, text = funds)
        self.labele.grid(row = 2, column = 2)
        self.labelf = Label(self.frame, text = totalGiven)
        self.labelf.grid(row=3, column = 2)
        self.labelg = Label(self.frame, text = rewards)
        self.labelg.grid(row=4, column = 2)

        self.donatButton = Button(self.frame, text = "Make Donation", command = self.donatButtonFunc)
        self.donatButton.grid(row = 5, column = 0)

        self.claimRewButton = Button(self.frame, text = "Claim Rewards", command = self.claimRewButtonFunc)
        self.claimRewButton.grid(row=5, column = 2)

        self.checkRewStatusButton = Button(self.frame, text = "Check Reward Status", command = self.checkRewStatusButtonFunc)
        self.checkRewStatusButton.grid(row = 5, column = 1)

    def donatButtonFunc(self):
        #implement function to open a pop-up window asking to type in receiving Hobo's name, then doing donation function from user class then updates homepage with new funds and tG
        return 0
    def claimRewButtonFunc(self):
        #implement function that runs claim rewards function from giver class then updates rewards and tG in homepage
        return 0
    def checkRewStatusButtonFunc(self):
        #implement function that opens a pop-up window that runs checkRewards function from Giver class
        return 0

class HoboHomePage(Frame):
    def __init__(self,master, Hobo):
        myFont = Font(master, family="Times New Roman", size=20, underline=1, weight="normal")
        myFont2 = Font(master, family="Times New Roman", size = 18)
        self.frame = Frame(master)
        self.frame.pack()

        self.title1 = Label(self.frame, text="Donation System", fg="white", bg="black")
        self.title1.configure(font=myFont)
        self.title1.grid(row=0, column=1)

        s1 = "{}(HOBO)".format(Hobo.getName())
        self.labela = Label(self.frame, text = s1)
        self.labela.configure(font = myFont2)
        self.labela.grid(row=1, column = 1)

        self.labelb = Label(self.frame, text = "Balance:")
        self.labelb.grid(row=2, sticky = E)
        self.labelc = Label(self.frame, text = "Total Cashed In:")
        self.labelc.grid(row=3, sticky = E)

        balance = "${}".format(Hobo.getBalance())
        tCI = "${}".format(Hobo.gettCI())
        self.labele = Label(self.frame, text = balance)
        self.labele.grid(row = 2, column = 2)
        self.labelf = Label(self.frame, text = tCI)
        self.labelf.grid(row=3, column = 2)

        self.checkDonations = Button(self.frame, text = "Check Donations", command = self.checkDonationsFunc)
        self.checkDonations.grid(row = 4, column = 0) #returns list of donations with name and amount from Giver

        self.cashInBalance = Button(self.frame, text = "Cash In Balance", command = self.cashInBalanceFunc)
        self.cashInBalance.grid(row = 4, column = 1)

    def checkDonationsFunc(self):
        #implement function that opens pop-up window that gives list of names of Givers that donated and how much they gave
        return 0
    def cashInBalanceFunc(self):
        #implement function that does cashIn from Hobo Class
        return 0

'''u = Hobo()
v = Giver()
root = Tk()
app = HoboHomePage(root, u)
app2 = GiverHomePage(root, v)
root.mainloop()'''
