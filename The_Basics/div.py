#!/usr/bin/python3
"""How many times a number goes into another number"""


num1 = int(input("Please enter a number above 100: "))
num2 = int(input("Please enter a number below 10: "))
div = num1 // num2
print("{:d} goes into {:d}, {:d} times".format(num2, num1, div))
