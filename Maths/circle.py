#!/usr/bin/python3
"""Calculate are of a circle using user input"""
import math


print("Area of a circle = π * radius * radius")
num = int(input("Enter radius of a circle: "))
area = math.pi * num * num
print(area)
