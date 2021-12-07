import turtle

SCREEN_WIDTH = 450
ETCH_A_SKETCH_WIDTH = SCREEN_WIDTH + 50
SCREEN_HEIGHT = 250
ETCH_A_SKETCH_HEIGHT = SCREEN_HEIGHT + 100
OUTER_CIRCLE = 50
INNER_CIRCLE = 25
QUARTER_CIRCLE = 90

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
pict.circle(INNER_CIRCLE, QUARTER_CIRCLE)
pict.forward(SCREEN_HEIGHT)
pict.circle(INNER_CIRCLE, QUARTER_CIRCLE)
pict.forward(SCREEN_WIDTH)
pict.circle(INNER_CIRCLE, QUARTER_CIRCLE)
pict.forward(SCREEN_HEIGHT)
pict.circle(INNER_CIRCLE, QUARTER_CIRCLE)

# Draw edge of machine
pict.penup()
pict.goto(-250, -150)
pict.pendown()

pict.width(5)
pict.forward(ETCH_A_SKETCH_WIDTH)
pict.circle(OUTER_CIRCLE, QUARTER_CIRCLE)
pict.forward(ETCH_A_SKETCH_HEIGHT)
pict.circle(OUTER_CIRCLE, QUARTER_CIRCLE)
pict.forward(ETCH_A_SKETCH_WIDTH)
pict.circle(OUTER_CIRCLE, QUARTER_CIRCLE)
pict.forward(ETCH_A_SKETCH_HEIGHT)
pict.circle(OUTER_CIRCLE, QUARTER_CIRCLE)

# Draw the knobs
pict.penup()
pict.goto(-250, -140)
pict.pendown()

pict.color('gray')
pict.width(4)
pict.circle(35)
pict.penup()
pict.forward(SCREEN_WIDTH + 50)
pict.pendown()
pict.circle(35)

# Draw the Etch A Sketch letters
pict.penup()
pict.left(180)
pict.forward(250)
pict.right(90)
pict.forward(25)
pict.pendown()

pict.color('blue')
style = ('Arial', 30, 'bold italic')
pict.write('Etch A Sketch', font=style, align='center')

'''
Make this the last part of the code!
'''
my_screen = turtle.Screen()
my_screen.exitonclick()
