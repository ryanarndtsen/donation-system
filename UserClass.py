#general methods for password check
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def hasCapitals(inputString):
    return any(char.isupper() for char in inputString)

class Password(object):
    def __init__(self, passw= ""):
        self.password = passw
    def __repr__(self):
        return self.password
    def changePassword(self, p):
        self.password = p
    def checkPassword(self):
        password = self.password
        if hasCapitals(password) and hasNumbers(password) and len(password) >= 6:
            print("Strong password!")
        if len(password) < 6:
            print("Make sure your password is at least 6 letters.")
        if not hasNumbers(password):
            print("Make sure your password has a number in it.")
        if not hasCapitals(password): 
            print("Make sure your password has a capital letter in it.")
        if len(password) < 6 or not hasNumbers(password) or not hasCapitals(password):
            x = input("Enter new password:")
            self.password = x
            self.checkPassword()

class User(object):
    def __init__(self, firstName = "", lastName = "", age = 0, ID = [0,0,0,0], password = ""):
        self.firstName, self.lastName, self.age, self.ID = firstName, lastName, age, ID
        self.password = Password(password)
    def check_name(self):
        if self.firstName == "":
            print("First name was not specified.")
        if self.lastName == "":
            print("Last name was not specified.")
        if not self.lastName == "" and not self.firstName == "":
            print("Names are specified.")
    def __repr__(self):
        return "Name:{first} {last} \n Age:{age} \n ID: {ID} \n Password: {passw}".format(first = self.firstName, last= self.lastName, age = self.age, ID = self.ID, passw = "*" * len(self.password.password))
    def getName(self):
        return self.firstName + " " + self.lastName
    def setID(self, a, b, c, d):
        self.ID[0] = a
        self.ID[1] = b
        self.ID[2] = c
        self.ID[3] = d
    def setName(self, a, b):
        self.firstName = a
        self.lastName = b
    def setAge(self, a):
        self.age = a
    def getAge(self):
        return self.age
    def getID(self):
        idd = ""
        for i in self.ID:
            idd += str(i)
        return idd
    def setPassword(self, a):
        self.password.changePassword(a)
    def checkPass(self):
        self.password.checkPassword()
    def getPassword(self):
        return self.password.password

#test User
'''me = User("Ryan","Arndtsen", 19, [4,5,4,7], "Ryan999")
print(me)
print(me.getPassword())
me.setID(1,2,3,4)
me.setAge(10)
me.setName(me.firstName,"Swag")
print(me)
you = User("", "", 14, [3,2,2,2])
you.check_name
print('\n')'''

class Giver(User):
    def __init__(self, firstName = "", lastName = "", age = 0, ID = [0,0,0,0], password = "", funds = 0, totalGiven = 0, rewards = []):
        User.__init__(self, firstName, lastName, age, ID, password)
        self.funds = funds
        self.tG = totalGiven
        self.rewards = rewards
    def __repr__(self):
        return User.__repr__(self) + "\n Funds: {f} \n Rewards = {r}".format(f = self.funds, r = self.rewards)
    def addFunds(self, a):
        self.funds += a
    def getFunds(self):
        return self.funds
    def donate(self, a):
        self.funds -= a
        self.tG += a
    def gettG(self):
        return self.tG
    def rewardStatus(self):
        if self.tG < 100:
            return "No reward"
        elif self.tG >= 100 and self.tG < 200:
            return "Medium reward"
        else:
            return "Big reward"
    def claimReward(self):
        if self.rewardStatus() == "No reward":
            self.tG = 0
            return "Yikes"
        elif self.rewardStatus() == "Medium reward":
            self.rewards.append("Med")
            self.tG = 0
            return "Medium reward claimed"
        else:
            self.rewards.append("Big")
            self.tG = 0
            return "Big reward claimed"
    def checkRewards(self):
        return self.rewards

#test Giver
"""hi = Giver("Frank","Ocean", 13, [1,1,1,1], "hellO666", 1500, 14, [])
hi.checkPass()
print(hi)
print(hi.addFunds(20))
print(hi.getFunds())
print(hi.donate(143))
print(hi.gettG())
print(hi.rewardStatus())
print(hi.claimReward())
print(hi.checkRewards())
print('\n')"""

class Hobo(User):
    def __init__(self, firstName = "", lastName = "", age = 0, ID = [0,0,0,0], password = "", balance = 0, totalCashedIn = 0):
        User.__init__(self, firstName, lastName, age, ID, password)
        self.balance = balance
        self.tCI = totalCashedIn
    def __repr__(self):
        return User.__repr__(self) + "\n Balance: {bal}".format(bal = self.balance)
    def updateBalance(self, a):
        self.balance += a
    def getBalance(self):
        return self.balance
    def cashIn(self):
        if self.balance <= 0:
            return "No funds to cash in."
        self.tCI += self.balance
        self.balance = 0
    def gettCI(self):
        return self.tCI

#test Hobo
rob = Hobo("Ronald","Weasley", 42, [10,22,3,1], "exntoP69", 0, 10)
print(rob)
rob.updateBalance(5)
print(rob.getBalance())
print(rob.cashIn())
print(rob.gettCI())
print("\n")

#additional methods
def donation(Giver, Hobo, amount):
    if Giver.getFunds() < amount:
        print("Insufficient funds")
    else:
        Giver.donate(amount)
        Hobo.updateBalance(amount)
        print("Thank you for your donation.")
def log_in(User):               #might have to change when implementing database
    x = input("Enter ID:")
    y = input("Enter Password:")
    if x == User.getID() and y == User.getPassword():
        print("Welcome {n}".format(n = User.getName()))
    else:
        if x != User.getID():
            print("Incorrect ID")
        if y != User.getPassword():
            print("Incorrect Password")
        log_in(User)






        
