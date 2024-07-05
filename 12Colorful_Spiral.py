# Colorful_Spiral.py

import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black

# Set up the turtle
spiral = turtle.Turtle()
spiral.speed(0)  # Set the drawing speed to the fastest
spiral.width(2)  # Set the pen size

# List of colors to use in the pattern
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "pink"]

# Function to draw a colorful spiral
def draw_spiral():
    for i in range(360):
        spiral.color(random.choice(colors))  # Choose a random color from the list
        spiral.forward(i * 2)  # Move the turtle forward
        spiral.right(91)  # Turn the turtle right by 91 degrees

# Position the turtle at the center
spiral.penup()
spiral.goto(0, 0)
spiral.pendown()

# Draw the spiral pattern
draw_spiral()

# Finish drawing
turtle.done()  # Keep the window open until closed by the user
