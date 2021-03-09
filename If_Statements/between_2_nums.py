#!/usr/bin/python3
"""number input should be between 10 and 20(inclusive)"""


num = int(input("Enter number between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")
