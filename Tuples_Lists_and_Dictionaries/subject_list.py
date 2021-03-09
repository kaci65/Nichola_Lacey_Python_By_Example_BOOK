#!/usr/bin/python3
"""Remove item from list. Display list"""


subjects = ["Maths", "English", "Swahili", "Biology", "Chemistry", "Physics"]
print(subjects)
name = input("Which of the above subjects don't you like?: ")
subjects.remove(name)
print(subjects)
