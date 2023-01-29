# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
count = 0
for height in student_heights:
    sum += height
    count = count+1
avg = round(sum / count)
print(avg)

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)

###############################################################

# for number in range (1, 101, 3):
#     print(number)

total_even = 0
for number in range (1, 101):
    if number % 2 == 0:
        total_even += number
print(total_even)

total_even = 0
for number in range (2, 101, 2):
    total_even += number
print(total_even)

##############################################################

# FIZZ BUZZ CHALLENGE

for n in range (1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

##################################################################

#Password Generator Project


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# letters_random = ""

# for l in letters:
#     if len(letters_random) < nr_letters:
#         letters_random += letters[random.randint(0, len(letters)-1)]

# # for l in range(1, nr_letters + 1):
# #      letters_random += random.choice(letters)

# symbols_random = ""

# for s in symbols:
#     if len(symbols_random) < nr_symbols:
#         symbols_random += symbols[random.randint(0, len(symbols)-1)]

# # for s in range(1, nr_symbols + 1):
# #      symbols_random += random.choice(symbols)

# numbers_random = ""

# for n in numbers:
#     if len(numbers_random) < nr_numbers:
#         numbers_random += numbers[random.randint(0, len(numbers)-1)]

# # for n in range(1, nr_numbers + 1):
# #      numbers_random += random.choice(numbers)

# password = letters_random + symbols_random + numbers_random
# password = ''.join(random.sample(password,len(password)))
# print(password)
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
password = ""

for l in range(1, nr_letters + 1):
     password_list.append(random.choice(letters))


for s in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for n in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
    password += char

print(password)