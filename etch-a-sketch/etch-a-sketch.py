import turtle

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 250

pict = turtle.Turtle()
pict.speed(10)
pict.shape('circle')
pict.color('red')
pict.width(3)
pict.turtlesize(0.25)

pict.penup()
pict.goto(-230, -40)
pict.down()
pict.forward(SCREEN_WIDTH)
pict.left(90)
pict.forward(SCREEN_HEIGHT)


'''
Make this the last part of the code!
'''
my_screen = turtle.Screen()
my_screen.exitonclick()
