#!/usr/bin/python3
"""Draw 3 squares with spaces between them"""
import turtle


t = turtle.Turtle()
t.color("black", "pink")
t.begin_fill()
for i in range(4):
    t.forward(85) #forward by 100 units
    t.left(90) #turn at 90 degree angle
t.penup()
t.end_fill()
t.forward(110)

t.pendown()
t.color("black", "purple")
t.begin_fill()
for i in range(4):
    t.forward(85)
    t.left(90)
t.penup()
t.end_fill()
t.forward(110)

t.pendown
t.color("black", "sky blue")
t.begin_fill()
for i in range(4):
    t.forward(85)
    t.left(90)
t.end_fill()
turtle.exitonclick()
