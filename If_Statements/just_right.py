#!/usr/bin/python3
"""check if number is less than or greter than"""


num = int(input("Enter number: "))
if num < 10:
    print("Too low")
elif num > 10 and num < 20:
    print("Correct")
else:
    print("Too high")
