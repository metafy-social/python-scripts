#Import libraries and modules
from turtle import *

state = {'turn': 0}

# Function to spin the fidget
def spinner():
    clear()
    angle = state['turn']/8
    right(angle)
    forward(100)
    # Declare first dot
    dot(200, 'teal')
    back(100)
    right(120)
    forward(100)
    # Declare second dot
    dot(200, 'peach puff')
    back(100)
    right(120)
    forward(100)
    # Declare third dot
    dot(200, 'navy')
    back(100)
    right(120)
    update()

# Function that slows down the widget with time and spins it
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)

# Flick the fidget based on number of clicks
def flick():
    state['turn']+=12

# Define window size
setup(520, 520, 370, 0)

hideturtle()
tracer(False)
width(20)

# Call the function with clicks on spacebar
onkey(flick, 'space')
listen()
animate()
done()

