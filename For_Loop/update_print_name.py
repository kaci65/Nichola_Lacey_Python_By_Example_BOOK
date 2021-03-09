#!/usr/bin/python3
"""
ask for user's name and a number. Display each letter in name
on separate line x number of times
"""


name = input("Enter your name: ")
num = int(input("Enter a number: "))

for i in range(0, num):
    for j in name:
        print(j)
