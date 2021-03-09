#!/usr/bin/python3
"""Add numbers together from user input only if user agrees"""


total = 0
for i in range(0, 5):
    num = int(input("Enter number: "))
    ques = input("Do you want this number included? Yes or No: ")
    if querry == "yes" or "Yes" or "YES":
        total = total + num
    else:
        pass
print("Total:", total)
