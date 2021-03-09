#!/usr/bin/python3
"""
ask for user's name and a number, display name x number
of times if number is less than 10
"""


name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0, 3):
        print("Too high")
