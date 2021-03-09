#!/usr/bin/python3
"""
Do math calculations on randomly chosen numbers. If correct, add 
a point to user's score
"""
import random

point = 0
for i in range(1, 6):
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    add = num1 + num2
    add_r = int(input("What is num1 + num2: "))
    if add_r == add:
        point = point + 1
print("You got {:d} correct answers out of five".format(point))
