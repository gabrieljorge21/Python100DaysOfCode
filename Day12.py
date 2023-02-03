from Day12_art import logo
import random
import os

EASY_LEVEL = 10
HARD_LEVEL = 5

def level(level):
    """Returns 5 attempts if 'high' and 10 if 'easy level'"""
    if level == "high":
        return HARD_LEVEL
    elif level == "easy":
        return EASY_LEVEL

def pick_number():
    return random.randint(0,100)

print(logo)

attempts = level(input("\nWhich level? 'high' or 'easy': "))

print(f"You have {attempts} attempts. The number is between 0 and 100")

picked_number = pick_number()

def check_winner(guess, picked_number):
    if guess > picked_number:
        return f"Lower...\nYou have {attempts} attempts remaining\n"
    elif guess < picked_number:
        return f"Higher...\nYou have {attempts} attempts remaining\n"
    else:
        return f"\nYEAH!!! YOU WIN. The number was {picked_number}"

guess = -1 
while guess != picked_number and attempts > 0:
    guess = int(input("Guess the number... "))
    attempts -=1
    print(check_winner(guess, picked_number))

# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()


