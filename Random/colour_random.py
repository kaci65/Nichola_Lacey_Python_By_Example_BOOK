#!/usr/bin/python3
"""Random colours from list of five"""
import random


colours = ["red", "green", "blue", "gold", "white"]
print(colours)
colour_r = random.choice(colours)
pick_c = input("Pick one colour: ")
while pick_c is not colour_r:
    if pick_c == "green":
        print("I bet you are GREEN with envy")
    elif pick_c == "blue":
        print("You are probably feeling BLUE right now")
    elif pick_c == "red":
        print("I bet you're seeing red right now. Calm down!")
    elif pick_c == "white":
        print("Don't raise the white flag! Try again, you got this")
    elif pick_c == "gold":
        print("This is a golden opportunity, to show you're a genius")
    pick_c = input("Pick another colour: ")
print("Well done")
