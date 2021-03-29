#!/usr/bin/python3
"""update sales_2D_dict.py: update region from user input"""


sales = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},"Anne":{"N":5239,"S":4802,"E":5820,"W":1859}, "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
print(sales)
row_name = input("Please select a name: ")
col_region = input("Please enter a region to change sales figure: ")
print(sales[row_name][col_region])
ques = input("Do you want to change the value shown? ")
ans = ["yes", "Yes", "YES", "y", "Y"]
if ques in ans:
    num = int(input("Please enter a new sales figure: "))
    sales[row_name][col_region] = num
print("The updated sales figure is: {}".format(sales[row_name]))
