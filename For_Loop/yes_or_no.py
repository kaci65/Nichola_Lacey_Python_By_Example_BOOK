#!/usr/bin/python3
"""Add numbers together from user input only if user agrees"""


total = 0
for i in range(5):
    num = int(input("Enter number: "))
    ques = input("Do you want this number included? Yes or No: ")
    ans = ["yes", "Yes", "YES"]
    if ques in ans:
        total = total + num
    else:
        break
print("Total:", total)
