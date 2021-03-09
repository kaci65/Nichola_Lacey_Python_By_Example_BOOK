#!/usr/bin/python3
"""Randomly choose heads or tails"""
import random


h_t = random.choice(["h", "t"])
ques = input("Choose heads or tails: h/t: ")
if h_t == ques:
    print("You win")
else:
    print("Bad luck")
