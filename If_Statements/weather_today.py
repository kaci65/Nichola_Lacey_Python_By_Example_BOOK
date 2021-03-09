#!/usr/bin/python3
"""Convert user input to lowercase, test a number of test cases"""


rainy = input("Is it raining? Answer Yes or No: ")
rainy = str.lower(rainy)
if rainy == "yes":
    windy = input("Is it windy? Answer Yes or No: ")
    windy = str.lower(windy)
    if windy  == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
