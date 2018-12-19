# Get libraries
import turtle as t
from random import randint
import sys
from tkinter import TclError

# Createan object to hold a snowflake
class Snowflake(object):

    # Constructor
    def __init__(self, x, y, r, fall):
        self.x = x
        self.y = y
        self.r = r
        self.fall = fall

# Create an empty function to be passed by default
def x():
    pass

# Create a snowglobe object
class Snowglobe(object):

    # Constructor
    def __init__(self, title, noSnowflakes, scene=x):

        # Create a list of snowflakes
        # and add snowflakes
        self.snowflakes = []
        for i in range(noSnowflakes):
            
            # Create a snowflake and add it
            self.snowflakes.append(Snowflake(randint(-290, 290), randint(300, 500), randint(1, 5), randint(1, 5)))

        # Set the function to draw the scene
        self.scene = scene

        # Set the height of the snow
        self.snowHeight = 100

        # Initialise the turtle
        t.hideturtle()
        t.title(title)
        t.tracer(0,0)
        t.bgcolor("#483d8b")

    # Create a function to update the snowglobe
    def update(self):

        try:

            # Clear the turtle
            t.clear()

            # Draw the scene
            self.scene()

            # Draw the background
            self.drawBackground()

            # Draw the snowflurry
            self.updateSnow()

            # Update turtle
            t.update()

        except TclError as e:
            
            print("Program exited successfully.")
            sys.exit()

    # Define a function to draw the background
    def drawBackground(self):

        # Draw the background
        t.penup()
        t.goto(-300, -300 + self.snowHeight)
        t.color("white")
        t.pendown()
        t.begin_fill()
        for side in range(2):
            t.forward(600)
            t.right(90)
            t.forward(self.snowHeight)
            t.right(90)
        t.end_fill()
        t.penup()
        t.goto(-300, 300)
        t.pendown()
        for side in range(2):
            t.forward(600)
            t.right(90)
            t.forward(600)
            t.right(90)

    # Define a function to update the snowglobe
    def updateSnow(self):

        # Look at each bit of snow and update it
        for s in self.snowflakes:

            # Move the snowflake
            s.y -= s.fall

            # Regenerate the snowflake if it has fallen to the bottom
            if s.y < - 300 + self.snowHeight - 10:
                s.y = randint(300, 500)
                s.fall = randint(1,5)
                s.radius = randint(1,5)

            # If the snowflake is on screen, draw it
            if s.y + 2 * s.r < 300:

                # Move the pen
                t.penup()
                t.goto(s.x, s.y + s.r)
                t.pendown()

                # Set the colour
                t.color("white")

                # Draw the filled in circle
                t.begin_fill()
                t.circle(s.r)
                t.end_fill()
        
