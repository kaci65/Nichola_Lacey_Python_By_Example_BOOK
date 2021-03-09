#!/usr/bin/python3
"""number input should be between 10 and 20"""


num = int(input("Enter number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too low")
    elif num > 20:
        print("Too high")
    num = int(input("Try again. Enter a number: "))
print("Thank you")
