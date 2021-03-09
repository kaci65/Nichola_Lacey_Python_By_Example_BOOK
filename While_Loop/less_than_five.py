#!/usr/bin/python3
"""If number input from user is over 5, display a text"""


num = 0
while num <= 5:
    num = int(input("Enter number: "))
print("The last number you entered  was a {:d}".format(num))
