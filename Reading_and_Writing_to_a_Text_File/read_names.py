#!/usr/bin/python3
"""Open the Names.txt file and display the data"""


file = open("Names.txt", "r")
print(file.read())
file.close()
