#!/usr/bin/python3
"""check if user input is correct the secondtime round"""


passwrd = input("Please enter password: ")
passwrd2 = input("Please confirm password: ")
if passwrd == passwrd2:
    print("Thank you")
elif passwrd.islower() != passwrd2.islower():
    print("They must be in the same case")
else:
    print("Incorrect")
