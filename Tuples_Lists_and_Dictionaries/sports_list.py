#!/usr/bin/python3
"""
Create list. Ask for user input, add it to the end of list.
Sort list. Display it
"""


sports_list = ["Hockey", "Badminton"]
sports_list.append(input("What is your favourite sport?: "))
sports_list.sort()
print(sports_list)
