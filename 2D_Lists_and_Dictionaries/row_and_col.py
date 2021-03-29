#!/usr/bin/python3
"""
update task 'simple_2D_list.py' and use user input to select row and column
"""


simple_array = [[2, 3, 1, 4], [5, 7, 6, 2], [8, 4, 9, 0]]
row = int(input("Please enter a row number: "))
col = int(input("Please enter column number: "))

print("The number on row {} column {} is {}".format(row, col, simple_array[row][col]))
