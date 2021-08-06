# # Exercise 1 (and Solution)
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

today_date=datetime.date.today()

print("Todays date is: "+ str(today_date))

name=input("What is you name?")

age=int(input("what is your age?"))

print(name+ "\nYour age is :", age)

hundredyrs=(int(today_date.year) + (100-age))

print("you will be 100 years old at the year", str(hundredyrs))