def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return month_days[month - 1] + 1
    else:
        return month_days[month - 1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

import os
from Day10_art import logo

def calculate(a, b, op):
	if op == "+":
		return a+b
	elif op == "-":
		return a-b
	elif op == "*":
		return a*b
	elif op == "/":
		return a/b
	elif op == "^":
		return a**b
	else:
		raise Exception ("Invalid option!")

def add(a, b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def pow(a,b):
    return a ** b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": pow,
}

for symbol in operations:
    print(symbol)

num1 = float(input("Num1?"))
num2 = float(input("Num2?"))
oprtn = input("What operation?")
function = operations[oprtn]
print(function(num1,num2))  

should_continue = True
continue_calc = False
try:
    while should_continue:
        os.system("clear")
        print(logo)
        if not continue_calc:		
            var1 = float(input("Enter a number: "))
        var2 = float(input("Enter next number: "))
        var3 = input("Enter the operator: ")
        res = calculate(var1, var2, var3)
        print(f"{var1} {var3} {var2} = {res}")
        aux = input(f"Type 'y' to continue with {res} or 'n' to reset: ")
        if aux == "y":
            continue_calc = True
            var1 = res
        else:
            continue_calc = False
except ZeroDivisionError:
        print("No se puede dividir entre 0")
except Exception as e:
        print(e)