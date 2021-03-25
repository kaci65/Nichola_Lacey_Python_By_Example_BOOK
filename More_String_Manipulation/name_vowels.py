#!/usr/bin/python3
"""find numbe of vowels in user input"""


name = input("What is your name? ")
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
count = 0
for i in name:
    if i in vowels:
        count += 1
print("Your name has {} vowels in it".format(count))
