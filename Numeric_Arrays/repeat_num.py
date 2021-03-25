#!/usr/bin/python3
"""Find how many times a number is repeated"""


from array import *
numArray = array('i', [])
numArray = [2, 3, 4, 2, 3]
print(numArray)
num = int(input("Enter any of the numbers shown: "))
if num in numArray:
        print("{} appears {} times in the array".format(num, numArray.count(num)))
