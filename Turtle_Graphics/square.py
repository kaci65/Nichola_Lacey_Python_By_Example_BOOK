#!/usr/bin/python3
"""Draw a square"""
import turtle


turtle.shape("turtle")
for i in range(4):
    #will run 4 times
    turtle.forward(100) #forward by 100 units
    turtle.left(90) #turn at 90 degree angle
turtle.exitonclick()
