#!/usr/bin/python3
"""
Calculate the area based on user input. If user input is not 1 or 2,
display error message
"""
import math


print("1) Square\n2) Triangle\n")
num = int(input("Enter a number: "))
if num == 1:
    length = int(input("Enter the square length: "))
    square_area = length * length
    print(square_area)
elif num == 2:
    base = int(input("Enter the base of a triangle: "))
    height = int(input("Enter the height of a triangle: "))
    tri_area = 0.5 * base * height
    print(tri_area)
else:
    print("Error: Please enter either 1 or 2")
