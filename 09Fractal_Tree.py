# Fractal_Tree.py

import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black

# Set up the turtle
tree = turtle.Turtle()
tree.color("green")  # Set the color of the tree
tree.speed(0)  # Set the drawing speed to the fastest
tree.hideturtle()  # Hide the turtle cursor for a cleaner look
tree.pensize(2)  # Set the pen size

# Function to draw a fractal tree
def draw_branch(branch_length, t):
    if branch_length > 5:  # Base case: branch length is too short
        t.forward(branch_length)  # Move turtle forward
        t.right(20)  # Turn right by 20 degrees
        draw_branch(branch_length - 15, t)  # Recursively draw the right branch
        t.left(40)  # Turn left by 40 degrees
        draw_branch(branch_length - 15, t)  # Recursively draw the left branch
        t.right(20)  # Turn right by 20 degrees to original heading
        t.backward(branch_length)  # Move turtle backward to original position

# Position the turtle
tree.penup()
tree.left(90)  # Point the turtle upwards
tree.backward(200)  # Move the turtle down a bit
tree.pendown()

# Start drawing the fractal tree
draw_branch(100, tree)  # Call the function to draw the tree

# Finish drawing
turtle.done()  # Keep the window open until closed by the user
