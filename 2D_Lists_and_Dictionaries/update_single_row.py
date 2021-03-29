#!/usr/bin/python3
"""update a row by appending a new value using user input"""


simple_array = [[2, 3, 1, 4], [5, 7, 6, 2], [8, 4, 9, 0]]
row = int(input("Please enter a row number: "))
print(simple_array[row])
num = int(input("Please enter a number: "))
simple_array[row].append(num)
print("The updated row is: {}".format(simple_array[row]))
