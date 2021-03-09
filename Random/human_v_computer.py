#!/usr/bin/python3
"""Random number between 1 and 5"""
import random


num = random.randint(1, 5)
num_r = int(input("Pick a number between 1 and 5: "))
if num == num_r:
    print("Well done")
elif num_r > num:
    print("Too high")
elif num_r < num:
    print("Too low")
num_r = int(input("Try again. Pick a second number: "))
if num == num_r:
    print("Correct")
else:
    print("You lose")
