#!/usr/bin/python3
"""check if num is 1, 2 or 3. Then display text based on number chosen"""


num = int(input("Please enter number 1, 2 or 3: "))
if num == 1:
    print("Thank you")
elif num == 2:
    print("Well done")
elif num == 3:
    print("Correct")
else:
    print("Error message")
