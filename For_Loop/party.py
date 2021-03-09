#!/usr/bin/python3
"""Check if user input exceeds ten"""


num = int(input("How many people do you want to invite to the party?: "))
if num < 10:
    for i in range(0, num):
        name = input("Enter name: ")
        print("{:s} has been invited".format(name))
elif num >= 10:
    print("Too many people")
