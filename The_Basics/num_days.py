#!/usr/bin/python3
"""Number of hours, minutes, seconds according to input of days"""


numDays = int(input("Enter number of days: "))
hours =  numDays * 24
minutes = hours * 60
seconds = minutes * 60
print("There are {:d} hours, {:d} minutes and {:d} seconds in {:d} days".format(hours, minutes, seconds, numDays))
