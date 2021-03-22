#!/usr/bin/python3
"""Check if user input matches num on the list and display the position"""


num_list = [345, 786, 841, 921]
for i in num_list:
    print(i)
user_num = int(input("Please enter a three digit number: "))
if user_num not in num_list:
    print("That is not on the list")
else:
    print("{:d} is in position".format(user_num), num_list.index(user_num))
