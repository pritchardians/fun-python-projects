import turtle
import random

turtle.colormode(255)


def randcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col_tup = (r, g, b)
    return col_tup


pic = turtle.Turtle()
pic.turtlesize(0.25)
pic.width(10)
pic.speed(10)

# Change these values for different walk experiences!
MIN_STEPS = 30
MAX_STEPS = 80
MIN_DEGREES_TURN = 1
MAX_DEGREES_TURN = 360
WALK_DRUNKEN = False  # True / False
MIN_STEP_DISTANCE = 5
MAX_STEP_DISTANCE = 100

for _ in range(0, random.randint(MIN_STEPS, MAX_STEPS)):
    if WALK_DRUNKEN:
        direction = (random.randint(MIN_DEGREES_TURN, MAX_DEGREES_TURN))
    else:
        direction = random.randint(0, 3) * 90
    pic.setheading(direction)
    # rand_red = random.randint(0, 100) / 100
    # rand_green = random.randint(0, 100) / 100
    # rand_blue = random.randint(0, 100) / 100
    # pic.color(rand_red, rand_green, rand_blue)
    pic.color(randcolor())
    pic.forward(random.randint(MIN_STEP_DISTANCE, MAX_STEP_DISTANCE))

### Make this last!
my_screen = turtle.Screen()
my_screen.exitonclick()
