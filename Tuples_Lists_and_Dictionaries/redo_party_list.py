#!/usr/bin/python3
"""Remove names from the list according to user input"""


names_list = []
for i in range(3):
    names_list.append(str(input("Please enter names of 3 people to invite to the party: ")))
ques1 = input("Do you want to invite anyone else? Yes or No: ")
ans1 = ["yes", "Yes", "YES", "y", "Y"]
while ques1 in ans1:
    names_list.append(str(input("Add another name to the list: ")))
    ques1 = input("Do you want to invite anyone else? Yes or No: ")
print("You have invited", len(names_list), "people")
for x in names_list:
    print(x)
del_name = input("Choose a name from the displayed list: ")
print("{:s} is at position".format(del_name), names_list.index(del_name))
ques2 = input("Do you still want this person at the party? Yes/No? ")
ans2 = ["NO", "No", "no", "N", "n"]
if ques2 in ans2:
    names_list.remove(del_name)
    for j in names_list:
        print(j)
