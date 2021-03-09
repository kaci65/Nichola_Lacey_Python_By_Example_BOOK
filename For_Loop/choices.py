#!/usr/bin/python3
"""Count up or down depending on user input"""


querry = input("Which direction do you want to count from? Up or Down?: ")
querry1 = querry.lower()
if querry1 == "up":
    num = int(input("Enter a high number: "))
    for i in range(1, num + 1, +1):
        print(i)
elif querry1 == "down":
    num = int(input("Enter a number below 20: "))
    for i in range(20, num - 1, -1):
        print(i)
else:
    print("Error: I don't understand")
