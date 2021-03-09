#!/usr/bin/python3
"""Add numbers together from user input, only if user agrees"""


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
add_nums = num1 + num2
ques = input("Do you want to add another number? Y/N: ")
ques_ = ques.lower()
while ques_ == "y":
    num_ = int(input("Enter another number: "))
    add_nums = add_nums + num_
    ques_ = input("Do you want to add another number? Y/N: ")
print("{:d}".format(add_nums))
