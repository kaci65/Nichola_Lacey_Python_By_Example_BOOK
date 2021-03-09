#!/usr/bin/python3
"""user input = name and age. Add 1 to their age"""


name = input("Enter name: ")
age = int(input("Enter age: "))
new_age = age + 1
print("{:s} next bithday you will be {:d}".format(name, new_age))
