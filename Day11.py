############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
u_hand = []
pc_hand = []

continue_game = True

u_hand.append(random.choice(deck))
u_hand.append(random.choice(deck))

pc_hand.append(random.choice(deck))

if sum(u_hand) == 21:
    print(f"BLACKJACK! You have: {u_hand}")
    print(f"PC has: {pc_hand} = {sum(pc_hand)}")
    continue_game = False


while continue_game:

    print(f"You have: {u_hand} = {sum(u_hand)}")
    print(f"PC has: {pc_hand} = {sum(pc_hand)}")


    opt = input("Type 'y' to get another card or 'n' to pass: ")
    if opt == "y":
        u_hand.append(random.choice(deck))
        if 11 in u_hand and sum(u_hand) > 21:
                index = u_hand.index(11)
                u_hand[index] = 1
        if sum(u_hand) > 21:
            print(f"You have: {u_hand} = {sum(u_hand)}")
            print(f"PC has: {pc_hand} = {sum(pc_hand)}")
            print("YOU LOSE")
            continue_game = False
    else:
        while sum(pc_hand) < 17:
            pc_hand.append(random.choice(deck))
            if 11 in pc_hand and sum(pc_hand) > 21:
                index = pc_hand.index(11)
                pc_hand[index] = 1
            if sum(pc_hand) >= 17:
                if sum(pc_hand) < sum(u_hand) or sum(pc_hand) > 21 and sum(pc_hand) != sum(u_hand):
                    print(f"You have: {u_hand} = {sum(u_hand)}")
                    print(f"PC has: {pc_hand} = {sum(pc_hand)}")
                    print("YOU WIN")
                    continue_game = False
                elif sum(pc_hand) > sum(u_hand) and sum(pc_hand) <= 21:
                    print(f"You have: {u_hand} = {sum(u_hand)}")
                    print(f"PC has: {pc_hand} = {sum(pc_hand)}")
                    print("YOU LOSE")
                    continue_game = False
                elif sum(pc_hand) == sum(u_hand):
                    print(f"You have: {u_hand} = {sum(u_hand)}")
                    print(f"PC has: {pc_hand} = {sum(pc_hand)}")
                    print("DRAW")
                    continue_game = False
