#!/usr/bin/python3
"""Slice list using start and end input numbers from user"""

colour_list = ["orange", "red", "yellow", "pink", "purple", "blue", "green", "white", "black", "brown"]
print(colour_list)
start_num = int(input("Please enter a starting number: "))
end_num = int(input("Please enter the ending number: "))
print(colour_list[start_num:end_num])
