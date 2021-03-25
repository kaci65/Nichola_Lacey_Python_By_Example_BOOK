#!/usr/bin/python3
"""array of generated random integers"""


from array import *
import random
nums = array('i', [])
for i in range(0, 5):
    nums.append(random.randint(1, 50))
for j in nums:
    print(j)
