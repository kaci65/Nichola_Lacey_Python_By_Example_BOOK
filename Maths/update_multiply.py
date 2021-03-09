#!/usr/bin/python3
"""Update multiply.py and show answer to two decimal places"""
import math


num = float(input("Enter a number with lots of decimal places: "))
mul = num * 2
print(mul)
new_mul = round(mul, 2)
print(new_mul)
