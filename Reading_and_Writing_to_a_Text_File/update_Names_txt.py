#!/usr/bin/python3
"""Update 'Names.txt' file using user input"""


file = open("Names.txt", "a")
newName = input("Please enter a new name: ")
file.write(newName + "\n")
print(file.read())
file.close()
