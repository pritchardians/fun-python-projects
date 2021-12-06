import turtle

SCREEN_WIDTH = 450
ETCH_A_SKETCH_WIDTH = SCREEN_WIDTH + 50
SCREEN_HEIGHT = 250
ETCH_A_SKETCH_HEIGHT = SCREEN_HEIGHT + 100

pict = turtle.Turtle()
pict.speed(10)
pict.shape('circle')
pict.color('red')
pict.width(3)
pict.turtlesize(0.25)

# Draw inner screen
pict.penup()
pict.goto(-230, -40)
pict.down()
pict.forward(SCREEN_WIDTH)
pict.left(90)
pict.forward(SCREEN_HEIGHT)
pict.left(90)
pict.forward(SCREEN_WIDTH)
pict.left(90)
pict.forward(SCREEN_HEIGHT)

# Draw edge of machine
pict.penup()
pict.goto(-250, -110)
pict.pendown()
pict.width(5)

pict.left(90)
pict.forward(ETCH_A_SKETCH_WIDTH)
pict.circle(25, 90)
pict.forward(ETCH_A_SKETCH_HEIGHT)
pict.left(90)
pict.forward(ETCH_A_SKETCH_WIDTH)
pict.left(90)
pict.forward(ETCH_A_SKETCH_HEIGHT)


'''
Make this the last part of the code!
'''
my_screen = turtle.Screen()
my_screen.exitonclick()
