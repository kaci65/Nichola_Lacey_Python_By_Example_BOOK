#!/usr/bin/python3
"""convert kilograms to pounds assuming there are 2.204 pounds in a kg"""


weight_kg = int(input("Enter number of kilograms: "))
pounds = weight_kg * 2.204
print("{:d} kilograms equals {:d} pounds".format(weight_kg, pounds))
