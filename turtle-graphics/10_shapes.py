from turtle import Turtle, Screen
import random

pict = Turtle()
pict.shape('circle')
pict.penup()
pict.goto(0, -100)
pict.pendown()

for shape_sides in range(3, 13):
    # New shape starts here
    pict.speed(shape_sides)
    pict.width(shape_sides * 2)
    # Choose random color for shape
    rand_red = random.randint(0, 100) / 100
    rand_green = random.randint(0, 100) / 100
    rand_blue = random.randint(0, 100) / 100
    pict.color(rand_red, rand_green, rand_blue)
    # pict.color(.100, .100, .100)
    degrees_to_turn = 360 / shape_sides
    for _ in range(1, shape_sides + 1):
        pict.left(degrees_to_turn)
        pict.forward(100)

'''
Make this the last part of the code!
'''
my_screen = Screen()
Screen().exitonclick()
