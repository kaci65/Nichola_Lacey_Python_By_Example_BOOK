#!/usr/bin/python3
"""display first two letters in uppercase"""


post_code = input("What is your postcode? ")
first_two = post_code[0:2]
the_rest = post_code[2:]
upper_first_two = first_two.upper()
combine = upper_first_two + the_rest
print(combine)
