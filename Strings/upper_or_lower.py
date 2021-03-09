#!/usr/bin/python3
"""Get input from user, check if input length is greater than or less than 5"""


firstname = input("Enter your firstname: ")
name_len = len(firstname)
if (name_len < 5):
    surname = input("Enter your surname: ")
    name = firstname + surname
    new_name = name.upper()
    print(new_name)
elif (name_len >= 5):
    new_firstname = firstname.lower()
    print(new_firstname)
