#!/usr/bin/python3
"""
Create dict, display dict, remove item from dict, sort dict, display dict
"""


food_dict = {}
food_dict[1] = input("Enter your favourite food: ")
food_dict[2] = input("Enter your second favourite food: ")
food_dict[3] = input("Enter your third favourite food: ")
food_dict[4] = input("Enter your fourth favourite food: ")
print(food_dict)
del_food = int(input("Which food do you want to delete? "))
del food_dict[del_food]
print({key: value for key, value in sorted(food_dict.items(), key=lambda item: item[1])})
