#!/usr/bin/python3
"""
Ask for user's name and a number. Display name x
number of times
"""


name = input("Enter your name: ")
num = int(input("Enter a number: "))

for i in range(0, num):
    print(name)
