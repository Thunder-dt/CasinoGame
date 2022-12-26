def addMoney(balance, amount):
    balance += amount
    return balance

def showMoney(balance):
    print("Your balance is: " + str(balance) +"$")

def playMoney(balance, cost):
    balance -= cost
    return balance

