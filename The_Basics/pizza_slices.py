#!/usr/bin/python3
"""Find out how many slices of pizza the user has left"""


initial_slices = input("Enter how many pizza slices you started with: ")
slices_eaten = input("Enter how many pizza slices you have eaten: ")
slices_left = int(initial_slices) - int(slices_eaten)
print("You have {:d} slices left".format(slices_left))
