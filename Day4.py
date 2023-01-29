import random
import os

# random_int = random.randint(0, 1)
# print(random_int)

# random_float = random.random()
# print(random_float)

# if random_int > 0:
#     print("Heads")
# else:
#     print("Tails")


# ############################################################

# # WHO PAYS THE BILL

# names_string = input("Enter the names separated by a comma: \n")
# names_list = names_string.split(", ")
# pick = random.randint(0, len(names_list)-1)
# print(f"{names_list[pick]} has to pay the bill!")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])

# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
# map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}\n")

# pos = input("Where to put an \"X\"? ")
# verti = int(pos[0])-1
# horiz = int(pos[1])-1
# map[verti][horiz] = "X"
# print(f"{row1}\n{row2}\n{row3}\n")


###############################################################

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
play_again = ""
wins = 0
loses = 0
draws = 0

while play_again == "":
    user = input("\nChoose 0 for Rock, 1 for Paper, 2 for Scissors: ")
    if not(user.isdigit()):
        print("\nIncorrect choise. YOU LOSE!")
        loses += 1
    else:
        user = int(user)
        if user > 2 or user < 0:
            print("\nIncorrect choise. YOU LOSE!")
            loses += 1
        else:
            pc = random.randint(0, 2)

            print("\nYOUR CHOISE:\n" + game[user]+"\n")
            print("COMPUTER CHOSE:\n" + game[pc]+"\n")

            if user == pc:
                print("😒 DRAW\n\n\n")
                draws += 1
            elif user == 0 and pc != 1:
                print("🥳 YOU WIN!\n\n\n")
                wins += 1
            elif user == 1 and pc != 2:
                print("🥳 YOU WIN\n\n\n")
                wins += 1
            elif user == 2 and pc != 0:
                print("🥳 YOU WIN\n\n\n")
                wins += 1
            else:
                print("😅 YOU LOSE!\n\n\n")
                loses += 1

            play_again = input("PLAY AGAIN? ")
            os.system('clear')
            if play_again != "":
                print(f"SCORES:\n\nWINS: {wins}\nDRAWS: {draws}\nLOSES: {loses}\n")
                break
