#!/usr/bin/python3
"""Join first name and surname, then find length"""


firstname = input("Enter first name: ")
print(len(firstname))
surname = input("Enter surname: ")
print(len(surname))
full_name = firstname + ' ' + surname
name_len = len(full_name)
print("Hello", full_name)
print("The length of your {:s} is {}".format(full_name, name_len))
