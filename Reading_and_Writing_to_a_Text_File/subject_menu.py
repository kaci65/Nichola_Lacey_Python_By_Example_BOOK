#!/usr/bin/python3
"""Create a file, "Subject.txt". Add to it using user input"""


print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
num = int(input("Make a selection: 1, 2 or 3: "))
num_list = [1, 2, 3]
if num == 1:
    file = open("Subject.txt", "w")
    subject = input("Please enter a subject: ")
    file.write(subject + "\n")
    file.close()
elif num == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
elif num == 3:
    file = open("Subject.txt", "a")
    newSubject = input("Please enter a new subject: ")
    file.write(newSubject + "\n")
    file.close()
else:
    print("The number you have chosen is out of range")
