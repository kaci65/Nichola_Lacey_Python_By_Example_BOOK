#!/usr/bin/python3
"""Array: numbers must be between 10 and 20"""


from array import *
numArray = array('i', [])
for i in range(0, 5):
    num = int(input("Please enter a number between 10 and 20: "))
    if num >= 10 and num <= 20:
        numArray.append(num)
    else:
        print("Outside the range")
print()
print("Thank you")
for i in numArray:
    print(i)
