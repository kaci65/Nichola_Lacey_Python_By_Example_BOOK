#!/usr/bin/python3
"""display characters between start and end point"""


poem_line = ("Incy Wincy Spider Went up the Water Spout")
print(poem_line)
start_num = int(input("Please enter a starting number: "))
end_num = int(input("Please enter the ending number: "))
print(poem_line[start_num:end_num])
