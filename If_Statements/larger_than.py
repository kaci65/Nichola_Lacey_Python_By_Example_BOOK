#!/usr/bin/python3
"""If num1 is larger than num2, display num2 first otherwise show num1"""


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)
