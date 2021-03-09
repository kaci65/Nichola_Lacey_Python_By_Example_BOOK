#!/usr/bin/python3
"""Decrement a number(10) using while loop"""


num = 10
while num > 0:
    print("There are {:d} green bottles hanging on the wall,".format(num))
    print("{:d} green bottles hanging on the wall".format(num))
    print("and if 1 green bottle should accidentally fall")
    num = num - 1
    ans = int(input("How many green bottles will be hanging on the wall?: "))
    if ans == num:
        print("There will be {:d} green bottles hanging on the wall".format(num))
    else:
        print("No, try again")
    if num == 0:
        print("There are no more green bottles hanging on the wall")
