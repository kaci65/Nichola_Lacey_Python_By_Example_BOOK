#!/usr/bin/python3
"""Decrement a number from user input"""


num = int(input("Enter a number below 50: "))
for i in range(50, num - 1, -1):
    print(i)
