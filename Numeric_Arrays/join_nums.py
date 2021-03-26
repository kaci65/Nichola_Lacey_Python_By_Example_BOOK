#!/usr/bin/python3
"""Join two arrays: from input and random. Display array items"""


from array import *
import random

numInput = array('i', [])
numRandom = array('i', [])
newArray = array('i', [])
for i in range(0, 3):
    numInput.append(int(input("Please enter any 3 numbers: ")))
for j in range(0, 5):
    numRandom.append(random.randint(1, 50))
numInput.extend(numRandom)
newArray = numInput
newArray = sorted(newArray)
for x in newArray:
    print(x)
