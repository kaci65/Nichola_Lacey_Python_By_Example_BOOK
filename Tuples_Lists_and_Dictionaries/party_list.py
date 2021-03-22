#!/usr/bin/python3
"""Append new names to the list from user input"""


names_list = []
for i in range(3):
    names_list.append(str(input("Please enter names of 3 people to invite to the party: ")))
ques = input("Do you want to invite anyone else? Yes or No: ")
ans = ["yes", "Yes", "YES", "y", "Y"]
while ques in ans:
    names_list.append(str(input("Add another name to the list: ")))
    ques = input("Do you want to invite anyone else? Y/N: ")
print("You have invited", len(names_list), "people")
