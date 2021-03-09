#!/usr/bin/python3
"""
Random number between 1 and 10. User to enter number until they choose picked random number
"""
import random


num = random.randint(1, 10)
num_r = int(input("Enter a number between 1 and 10: "))
while num_r is not num:
    num_r = int(input("Try again. Enter another number: "))
print(num_r)
