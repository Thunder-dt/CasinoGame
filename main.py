import money
import game

balance = 4
cost = 5

def showCost(cost):
    print("The spin cost is: " + str(cost) +"$")

       

print("------------------Casino Game------------------")
print(" -----------------Game Rules------------------")
print("The cost of a spin is: "+str(showCost(cost)))
print("If you get 3 alike youu win 100$")
print("If you get 2 alike youu win 50$")
print("If you don't get any alikes you lose \n")
play = input("Do you want to play? (y/n): ")
print("\n\n\n")

if play == 'y' :
    print("Type N to stop playing \n")
    money.showMoney(balance)
    showCost(cost)
    
    i = 0
    
    while(i != "n"):
        
        if (cost > balance):
        
            print("\nyou can't do a spin")
            deposit = input("Do you want to deposit (y/n):")
        
            if (deposit == 'y'):
                dp = int(input("How mutch do you wanna deposit:"))
                balance = money.addMoney(balance, dp)

            else :
                i = "n"
        

        if int(balance) >= 5:
            balance -= cost
            win = game.roll()
            balance += win
        
        money.showMoney(balance)
        i = input("Do you wanna continue playing (y/n): ")

    print(" \n The Game has ended")
    money.showMoney(balance)

else:
    print("It's okay to be a looooser! ")


'''
Future ideas:
Track your deposits then see if u won money or lost

'''