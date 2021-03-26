#!/usr/bin/python3
"""Find the index of a number in array"""


from array import *

numArray = array('i', [12, 3, 4, 5, 9])
for x in numArray:
    print(x)
num = int(input("Enter any of the numbers shown: "))
while num not in numArray:
    num = int(input("Try again. Please select a number from the array: "))
print("The number {} is at position {}".format(num, numArray.index(num)))
