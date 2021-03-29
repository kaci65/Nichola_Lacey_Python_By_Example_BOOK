#!/usr/bin/python3
"""delete row using user input from 2D dict"""


#!/usr/bin/python3
"""display names and ages from list apart from shoe size"""


#!/usr/bin/python3
"""Create a 2D dict from user input"""


p_details = {}
i = 0
while i < 4:
    p_name = input("Please enter person's name: ")
    p_age = int(input("Please enter person's age: "))
    p_shoe_size = int(input("Please enter person's shoe size: "))
    p_details[p_name] = {"Age":p_age, "Shoe size":p_shoe_size}
    i += 1
    print()
print(p_details)
print()
name = input("Enter person's name to delete details: ")
del p_details[name]
print()
print(p_details)
