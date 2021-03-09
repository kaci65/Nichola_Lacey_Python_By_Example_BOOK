#!/usr/bin/python3
"""Check if user input passes the test case"""


colour = input("Please enter favourite colour: ")
if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too")
else:
    print("I don't like {}, I prefer red".format(colour))
