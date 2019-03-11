from PasswordClass import *
from UserClass import *
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
'''hi = Giver("Frank","Ocean", 13, [1,1,1,1], "hellO666", 1500, 14, [])
hi.checkPass()
print(hi)
print(hi.addFunds(20))
print(hi.getFunds())
print(hi.donate(143))
print(hi.gettG())
print(hi.rewardStatus())
print(hi.claimReward())
print(hi.checkRewards())
print('\n')'''
