import random
import os
from Day7_words import words

picked_word = random.choice(words)
display = []
lives = 6
end_of_game = False

for char in picked_word:
    display.append("_")

while not end_of_game:
    os.system("clear")
    from Day7_art import logo
    print(logo)
    from Day7_art import stages
    print(stages[lives])
    print(''.join(display))
    guess = input("\nGuess a letter of the word... ").upper()
    for n in range(0, len(picked_word)):
        if guess == picked_word[n]:
            display[n] = guess
    if guess not in picked_word:
        lives -= 1
    if lives == 0 or "_" not in display:
        end_of_game = True
        os.system("clear")
        print(logo)
        print(stages[lives])
        print(''.join(display))
        if(lives == 0):
            print("\nGAME OVER :(\n")
        else:
            print("\nWINNER!!! :D\n")