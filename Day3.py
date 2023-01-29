year = int(input("Año?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Biciesto")
        else:
            print("No Biciesto")
    else:
        print("Biciesto")
else:
    print("No biciesto")


if (year % 4 == 0 and year %100 == 0 and year % 400 == 0):
    print("Biciesto")
elif(year % 4 == 0 and year % 100 == 0):
    print("No biciesto")
elif(year % 4 == 0 and year % 100 != 0):
    print("Biciesto")
elif(year % 4 != 0):
    print("No biciesto")


def leap(year):
    if year % 4 == 0 and (year % 4 != 0 or year % 400 == 0):
        return True
    return False

########################################################################

bill = 0
size = input("Size?\n")
add_pep = input("Pep?\n")
extra = input("Extra?\n")

if size == "l":
    bill += 25
elif size == "m":
    bill += 20
elif size == "s":
    bill += 15

if extra == "s":
    bill+=2
else:
    bill+=3

if extra == "y":
    bill += 1

print(f"{bill}")

####################################################

name1 = input("One name\n").lower()
name2 = input("Other name\n").lower()
names = name1 + name2

sum1 = 0
sum1 = names.count("t")
sum1 += names.count("r")
sum1 += names.count("u")
sum1 += names.count("e")

sum2 = 0
sum2 = names.count("l")
sum2 += names.count("o")
sum2 += names.count("v")
sum2 += names.count("e")

tot= int(str(sum1)+str(sum2))

if tot < 10 and tot>90:
    print(f"Boom {tot}")
elif tot >= 40 and tot <= 50:
    print(f"Excellent {tot}")
else:
    print(f"Nice {tot}")

#######################################################################
print("\n\n\n\n\n")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Left or right? ").lower()

if direction == "left":
    go = input("Swim or wait? ").lower()
    if go == "wait":
        door = input("Door Red, Yellow or Blue? ").lower()
        if door == "red":
            print("Fire! Game over.")
        elif door == "yellow":
            print("You WIN!")
        elif door == "blue":
            print("Eaten by beast! Game over")
        else:
            print("Game over")
    else:
        print("Attacked by shark! Game over.")

else:
    print("Fall into hole! Game over")