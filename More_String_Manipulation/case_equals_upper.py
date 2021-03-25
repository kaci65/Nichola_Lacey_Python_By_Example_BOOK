#!/usr/bin/python3
"""user input must be uppercase"""


word = input("Please enter any word: ")
if (word.islower()):
    word = input("Try again. This time in uppercase: ")
    print(word)
else:
    print(word)
