#!/usr/bin/python3
"""ask for user's first name and then surame. Change case to title"""


name1 = input("Enter first name in lowercase: ")
name2 = input("Enter surname in lowercase: ")

firstname = name1.title()
surname = name2.title()
name = firstname + " " + surname
print(name)
