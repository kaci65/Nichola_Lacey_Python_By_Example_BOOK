#!/usr/bin/python3
"""Change user input into Pig Latin"""


word = input("Enter any word: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
first_char = word[0]
if (first_char in vowels):
    new_word = word + "way"
    print(new_word.lower())
else:
    first_char = word[0:1]
    others = word[1:]
    new_word = others + first_char + "ay"
    print(new_word.lower())
