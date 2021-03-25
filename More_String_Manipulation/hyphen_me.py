#!/usr/bin/python3
"""put a hyphen after every letter"""


fave_subject = input("What is your favourite subject in school? ")
if fave_subject.encode().isalpha():
    for i in fave_subject:
        print(i, end="-")
