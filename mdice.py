import random

dfour = ["four", "4", "d4"]
dsix = ["six", "6", "d6"]
deight = ["eight", "8", "d8"]
dten = ["ten", "10", "d10"]
dtwelve = ["twelve", "12", "d12"]
dtwenty = ["twenty", "20", "d20"]
affirmatives = ["y", "yes"]
negatives = ["n", "no"]

print("""
mdice 0.1
You can choose from D4, a D6, a D8, D10, a D12 and a D20.
Press Ctrl-C to quit at any time.
""")

def dice_roll():
    roll = input("What die would you like to roll? ")
    if roll.lower() in dfour:
        print("You got:", random.randint(1,4))
    elif roll.lower() in dsix:
        print("You got:", random.randint(1,6))
    elif roll.lower() in deight:
        print("You got:", random.randint(1,8))
    elif roll.lower() in dten:
        print("You got:", random.randint(1,10))
    elif roll.lower() in dtwelve:
        print("You got:", random.randint(1,12))
    elif roll.lower() in dtwenty:
        print("You got:", random.randint(1,20))
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




