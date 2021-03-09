#!/usr/bin/python3
"""
Update country_tuple.py: Ask user to enter number. 
And then display country in that position.
"""


country_tuple = ("Kenya", "Egypt", "South Africa", "Namibia", "Uganda")
print(country_tuple)
name = input("Enter one of the countries shown: ")
print("{:s} is at index number".format(name), country_tuple.index(name))
num = int(input("Enter number between 0 and 4: "))
print(country_tuple[num])
