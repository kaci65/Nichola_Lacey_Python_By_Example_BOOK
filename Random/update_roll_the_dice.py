#!/usr/bin/python3
"""
update roll_the_dice.py
Random number between 1 and 10. User to enter number until they choose 
picked random number
Tell them if they are too hot or too cold
"""
import random


num = random.randint(1, 10)
num_r = int(input("Enter a number between 1 and 10: "))
while num_r is not num:
    if num_r > num:
        print("Too high")
    else:
        print("Too low")
    num_r = int(input("Try again. Enter another number: "))
print(num_r)
