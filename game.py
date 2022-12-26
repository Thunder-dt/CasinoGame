import random
def roll():    
    row = ["X","Y","Z","A","B"]

    i = random.randint(0, 4)
    r1 = row[i]

    i = random.randint(0, 4)
    r2 = row[i]

    i = random.randint(0, 4)
    r3 = row[i]

    resault = [r1,r2,r3]
    
    return resault

