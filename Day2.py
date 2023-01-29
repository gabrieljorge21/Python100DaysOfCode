#               DAY 2

two_digit_number=(input("Enter a 2 digit number\n"))
num1 = two_digit_number[0]
num2 = two_digit_number[1]
res= int(num1) + int(num2)
print("The result is " + num1 + " + " +num2 + " = " + str(res))

##################################################################

# PEMDA
# Parenthesis ()
# Exponent **
# Multiplication *
# Division /
# Addition +
# Substraction -

# BMI - Body Mass Index
weight= float(input("Enter your weigth in kg\n"))
height = float(input("Enter your heigth in m\n")) 
bmi = weight / (height**2)
print("BMI is " + str(bmi))
print("BMI is " + str(int(bmi)))
print("BMI is " + str(round(bmi,2)))
#floor division returns an int
print(10//2)
#common division returns a float
print(10/2)

#f-String
score = 0
isWinning = True
num = 1.03

print(f"The score is {score} and the number is {num} and is winning? {isWinning}")

#          LIFE IN WEEKS
age = int(input("Waht is your current age?\n"))
res = 90 - age
days = res * 365
weeks = res * 52
months = res * 12

print (f"You have {days} days or {weeks} weeks or {months} months left.")

#          TIP CALC
bill = float(input("How much is the bill?\n"))
tip =int(input("How much do you want for tip? 10, 12 or 15?\n"))
people = int(input("How many people?\n"))
bill = bill*(1 + tip/100)
bill /= people
print(f"Each person should pay {format(bill,'.2f')}")