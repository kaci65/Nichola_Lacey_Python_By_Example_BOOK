#!/usr/bin/python3
"""divide total of the bill by the number of diners"""


total = int(input("Enter total price of the dinner bill: "))
num_diners = int(input("Enter number of diners: "))
div_bill = total / num_diners
print("Each diner will pay $", div_bill)
