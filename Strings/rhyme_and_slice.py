#!/usr/bin/python3
"""Get input string from user, slice it using indexing then display it"""


string = input("Enter line of a nursery rhyme: ")
print(len(string))
begin = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
print(string[begin:end])
