#!/usr/bin/python3
"""type word backwords"""


word = input("Please enter a word: ")
letter = ""
for i in range(len(word) -1, -1, -1):
    print(word[i])
