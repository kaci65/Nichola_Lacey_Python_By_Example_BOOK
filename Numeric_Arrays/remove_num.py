#!/usr/bin/python3
"""Remove number from array"""


from array import *
oldArray = array('i', [])
newArray = array('i', [])
for i in range(0, 5):
    oldArray.append(int(input("Please enter any 5 numbers: ")))
oldArray = sorted(oldArray)
print(oldArray)
print()
del_num = int(input("Please select any number: "))
oldArray.remove(del_num)
print("{} has been removed from original array:".format(del_num))
print(oldArray)
print()
newArray = [del_num]
print("{} has been added to new array:".format(del_num))
print(newArray)
