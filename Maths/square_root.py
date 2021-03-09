#!/usr/bin/python3
"""Find square root of user input. Display it to two decimal places"""
import math


num = int(input("Enter a number over 500: "))
new_num = math.sqrt(num)
print(round(new_num, 2))
