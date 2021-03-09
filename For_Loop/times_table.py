#!/usr/bin/python3
"""Create a times table from user's input number"""


num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 12):
    print(num, 'x', i, '=', num * i)
