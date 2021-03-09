#!/usr/bin/python3
"""Check if user input is similar to the value of the variable"""


compNum = 50
num = int(input("Enter a number: "))
count = 1
while num != compNum:
    if num > compNum:
        print("Too high")
    else:
        print("Too low")
    count = count + 1
    num = int(input("Try again. Enter a number: "))
print("Well done, you took {:d} attempts".format(count))
