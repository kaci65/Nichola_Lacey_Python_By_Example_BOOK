#!/usr/bin/python3
"""Create tuple containing names of 5 countries. Display tuple"""


country_tuple = ("Kenya", "Egypt", "South Africa", "Namibia", "Uganda")
print(country_tuple)
name = input("Enter one of the countries shown: ")
print("{:s} is at index number".format(name), country_tuple.index(name))
