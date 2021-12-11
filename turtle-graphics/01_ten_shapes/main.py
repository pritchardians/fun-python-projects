import turtle
from funs import shapes

pic = turtle.Turtle()
pic.shape('circle')
pic.penup()
pic.goto(0, -100)
pic.pendown()
for sides in range(3, 13):
    shapes.draw_shape(pic, sides)

'''
Make this the last part of the code!
'''
my_screen = turtle.Screen()
my_screen.exitonclick()
