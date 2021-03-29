#!/usr/bin/python3
"""update a column by appending a new value using user input"""


simple_array = [[2, 3, 1, 4], [5, 7, 6, 2], [8, 4, 9, 0]]
row = int(input("Please enter a row number: "))
print(simple_array[row])
col = int(input("Please enter column number: "))
print(simple_array[row][col])
ques = input("Do you want to change the value shown? ")
ans = ["yes", "Yes", "YES", "y", "Y"]
if ques in ans:
    num = int(input("Please enter a new number: "))
    simple_array[row][col] = num
print("The updated row is: {}".format(simple_array[row]))
