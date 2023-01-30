# # #Write your code below this line 👇
# # import math

# # def paint_calc(height, width, cover):
# #     cans = math.ceil((height * width) / cover)
# #     print(f"You need {cans} of painting")

# # #Write your code above this line 👆
# # # Define a function called paint_calc() so that the code below works.   

# # # 🚨 Don't change the code below 👇
# # test_h = int(input("Height of wall: "))
# # test_w = int(input("Width of wall: "))
# # coverage = 5
# # paint_calc(height=test_h, width=test_w, cover=coverage)

# ####################### PRIMES ###########################

# #Write your code below this line 👇

# def prime_checker(number):
#     count = 2
#     control = True
#     while control:
#         if  count == number:
#             print("Prime")
#             control = False
#         elif number % count == 0:
#             print("Not Prime")
#             control = False
#         count += 1

# def prime_checker(number):
#     prime = True
#     for x in range (2, number):
#         if number % x == 0:
#             prime = False
#     if prime:
#         print("Prime")
#     else:
#         print("Not Prime")
    

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

################### CAESAR CIPHER ######################
from Day8_art import logo
import os

# def encrypt(text, shift):
#     cypher_text = ""
#     # for char in text:
#     #     for x in range(0, len(alphabet)):
#     #         if char == alphabet[x]:
#     #             encrypted_text += alphabet[x+shift]
#     for char in text:
#         pos = alphabet.index(char) - len(alphabet) + shift
#                     #a=0           -     26        +   1   = -25
#         cypher_text += alphabet[pos]
#     print(cypher_text)

# def decrypt(text, shift):
#     # decrypted_text = ""
#     # for char in text:
#     #     for x in range(0, len(alphabet)):
#     #         if char == alphabet[x]:
#     #             decrypted_text += alphabet[x-shift]
#     for char in text:
#         decrypted_text = ""
#         for char in text:
#             pos = alphabet.index(char) - shift
#             decrypted_text += alphabet[pos]
#     print(decrypted_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    new_text= ""
    if direction == "decode":
            shift *= -1
    for char in text:
        if char not in alphabet:
            new_text += char
        else:  
            pos = alphabet.index(char)
            pos = pos + shift
            new_text += alphabet[pos]
    print(f"\n---> The {direction}d text is [{new_text}] <---")

os.system("clear")
print(logo)

opt = "yes"
while opt == "yes":
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction, text, shift)
    opt = input("\nContinue? ")

os.system("clear")



