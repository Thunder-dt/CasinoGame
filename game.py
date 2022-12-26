import random
def roll():    
    row = ["X","Y","Z","A","B"]
    win = 0

    i = random.randint(0, 4)
    r1 = row[i]

    i = random.randint(0, 4)
    r2 = row[i]

    i = random.randint(0, 4)
    r3 = row[i]

    resault = [r1,r2,r3]
    print(resault)

    if (r1 == r2 and r1 == r3):
        print("You win 100$")
        win = 100

    else :
        
        if (r1 == r2 or r1 == r3 or r2 == r3):
            print("You win 50$")
            win = 50
        
        else:
            print("You lost")
    
    return win


