#!/usr/bin/python3
"""Add number from user input to total, while total is 50 or less"""


total = 0
while total <= 50:
    num = int(input("Enter number: "))
    total = total + num
    print("The total is... {:d}".format(total))
