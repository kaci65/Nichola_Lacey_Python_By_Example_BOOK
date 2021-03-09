#!/usr/bin/python3
"""Use whole number division and remainder"""
import math


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

div = num1 // num2
rem = num1 % num2
print("{:d} divided by {:d} is {:d} with {:d} remaining".format(
    num1, num2, div, rem))
