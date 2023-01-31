# ##Python Dictionaries

# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again.",
# }

# #Retrieving items from dictionary.
# # print(programming_dictionary["Function"])

# #Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# #Create an empty dictionary.
# empty_dictionary = {}

# #Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary)

# #Loop through a dictionary
# # for key in programming_dictionary:
# #   print(key)
# #   print(programming_dictionary[key])

# #######################################

# #Nesting 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# #Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, total_visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities
    new_country["total_visits"] = total_visits
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

import os
#HINT: You can call clear() to clear the output in the console.
from Day9_art import logo
print(logo)

bidders = []
should_continue = True

def add_bidder(name, value):
    new_bidder = {}
    new_bidder["name"]= name
    new_bidder["price"] = value
    bidders.append(new_bidder)

def find_highest_bidder():
    print(bidders)
    max_bid = 0
    name=""
    value=0
    for bidder in bidders:
        if bidder["price"] > max_bid:
            name = bidder["name"]
            max_bid = bidder["price"]

    print(f"\nThe winner is {name} with a bid of ${max_bid}")   

while should_continue:
    name = input("What's your name?: ")
    value = int(input("What's your bid?: $"))
    add_bidder(name, value)
    opt = input("Are there any other biggers? ")
    if opt == "no":
        should_continue = False
    os.system("clear")

find_highest_bidder()

