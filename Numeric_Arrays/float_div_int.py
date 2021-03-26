#!/usr/bin/python3
"""divide a float array with an integer from user input"""


from array import *
import math

floatNums = array('f', [34.53, 27.47, 87.25, 10.62, 73.56])
num = int(input("Please enter a number between 2 and 5: "))
for i in range(0, 5):
    if num >= 2 and num <= 5:
        div = floatNums[i] / num
        ans = round(div, 2)
        print("{} divided by {} is {}".format(floatNums[i], num, ans))
    else:
        print("The number you have chosen is out of range. Try again: ")
