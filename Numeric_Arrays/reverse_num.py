#!/usr/bin/python3
"""sort array and display it in reverse order"""


from array import *
num_array = array('i', [])
for i in range(0, 5):
    num_array.append(int(input("Please enter five integers: ")))
num_array = sorted(num_array)
num_array.reverse()
print(num_array)
