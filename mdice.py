import random

dfour = ["four", "4", "d4"]
dsix = ["six", "6", "d6"]
deight = ["eight", "8", "d8"]
dten = ["ten", "10", "d10"]
dtwelve = ["twelve", "12", "d12"]
dtwenty = ["twenty", "20", "d20"]
dhund = ["hundred", "one hundred", "100", "d100"]
dthou = ["thousand", "one thousand", "1000", "1,000", "d1000"]
affirmatives = ["y", "yes"]
negatives = ["n", "no"]
dx = ["dx"]

d4 = random.randint(1,4)
d6 = random.randint(1,6)
d8 = random.randint(1,8)
d10 = random.randint(1,10)
d12 = random.randint(1,12)
d20 = random.randint(1,20)
d100 = random.randint(1,100)
d1000 = random.randint(1,1000)

print("""
mdice 0.1
You can choose from D4, D6, D8, D10, D12, D20, D100 & D1000.
For multiple rolls, choose DX. 
Press Ctrl-C to quit at any time.
""")

def dice_roll():
    roll = input("What die would you like to roll? ")
    if roll.lower() in dfour:
        print("You got:", d4)
    elif roll.lower() in dsix:
        print("You got:", d6)
    elif roll.lower() in deight:
        print("You got:", d8)
    elif roll.lower() in dten:
        print("You got:", d10)
    elif roll.lower() in dtwelve:
        print("You got:", d12)
    elif roll.lower() in dtwenty:
        print("You got:", d20)
    elif roll.lower() in dhund:
        print("You got:", d100)
    elif roll.lower() in dthou:
        print("You got:", d1000)

    elif roll.lower() in dx:
        mult1 = input("Okay, a multi-roll. What die? ")
        mult2 = input("How many rolls? ")
        return 

    else: 
        print("That's not a die I recognize.")
        dice_roll()

dice_roll()

repeat = True
while repeat: 
    again = input("Roll again? ") 
    if again.lower() in affirmatives:
        dice_roll()
    elif again.lower() in negatives:
        print("""Alright then. Goodbye.
            """)
        break
    else:
        print("I'm sorry, I don't understand. ")
        dice_roll()
