#!/usr/bin/python3
""" Modify 'Names.txt' file using user input and rename to 'Names2.txt' """


file = open("Names.txt", "r")
print(file.read())
file.close()

name_del = input("Please choose one name: ")

