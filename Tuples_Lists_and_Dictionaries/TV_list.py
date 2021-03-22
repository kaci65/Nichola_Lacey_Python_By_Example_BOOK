#!/usr/bin/python3
"""Insert new programme at index from user's input"""


tv_list = ["Reply 1988", "Last", "Boku no hero", "Kimetsu no Yaiba"]
new_tv_list = []
for i in tv_list:
    print(i)
print()
new_show = input("Please enter another TV show: ")
show_pos = int(input("Enter position to insert show into TV list btn 0 - 4: "))
print()
new_tv_list = tv_list.insert(show_pos, new_show)
for j in tv_list:
    print(j)
