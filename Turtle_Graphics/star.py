#!/usr/bin/python3
"""Draw a five-pointed star"""
import turtle


t = turtle.Turtle()
t.color("black", "cyan")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.left(144)
t.end_fill()
turtle.exitonclick()
