#!/usr/bin/python3
"""Get user input and calculate volume of a cylinder"""
import math


print("volume of a cylinder = area of circle * depth/height")
radius = int(input("Enter radius of circle: "))
height = int(input("Enter depth of cylinder: "))
area_circle = math.pi * radius * radius
volume = area_circle * height
print(round(volume, 3))
