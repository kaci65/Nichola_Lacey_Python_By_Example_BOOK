#!/usr/bin/python3
"""Add user input to end of list. If user wants, delete last number entered"""


nums = []
i = 0
while i < 3:
    add_num = int(input("Please enter any numbers: "))
    nums.append(add_num)
    i = i + 1
print(nums)
ques = input("Do you want to save the last number? Y/N? ")
ans = ["NO", "No", "no", "N", "n"]
if ques in ans:
    nums.pop(i - 1)
    print(nums)
