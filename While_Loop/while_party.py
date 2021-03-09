#!/usr/bin/python3
"""Ask for a name and and 1 to count until user declines"""


ans_Y = ["yes", "YES", "y", "Y"]
ans = ans_Y
count = 0
while ans == ans_Y:
    name = input("Enter name: ")
    print("{:s} has now been invited".format(name))
    count = count + 1
    ans = input("Do you want to invite anyone else? Y/N: ")
print("{:d} have been invited to the party".format(count))
