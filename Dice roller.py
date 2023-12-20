from random import randint
dice = ["d100", "d20", "d12", "d10" , "d8" , "d6", "d4"]
print(dice)
roll = input("what dice do you want to roll?\n")
def Dice_roller():
    d20 = randint(1, 20)
    d4 = randint(1, 4)
    d6 = randint(1, 6)
    d8 = randint(1, 8)
    d10 = randint(1, 10)
    d12 = randint(1, 12)
    d100 = randint(1, 100)
    if roll == "d20":
        print(d20)
    elif roll == "d4":
        print(d4)
    elif roll == "d6":
        print(d6)
    elif roll == "d8":
        print(d8)
    elif roll == "d10":
        print(d10)
    elif roll == "d12":
        print(d12)
    elif roll == "d100":
        print(d100)
    return roll
