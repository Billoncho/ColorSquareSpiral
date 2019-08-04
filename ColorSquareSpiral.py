# ColorSquareSpiral.
# Billy Ridgeway
# Creates a colorful square spiral.

import turtle               # Imports turtle graphics.
t = turtle.Pen()            # Creates a new turtle called t.
turtle.bgcolor("black")     # Sets the background color to black.
t.speed(0)                  # Sets the pen's speed to fast.

# Creates a list of colors.
colors = ["red", "yellow", "blue", "green"]

# Creates a for loop.
for x in range (100):               # Sets the variable 'x' to 100.
    t.pencolor( colors[ x % 4] )    # Cycle through the pen's colors.
    t.forward(2*x)                  # Moves the pen forward 2 times the
                                    # value of 'x'.
    t.left(91)                      # Turns the pen left 91 degrees.
