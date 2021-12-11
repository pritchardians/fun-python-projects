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
step_size = 3

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

# Place cursor inside screen
pict.penup()
pict.color('black')
pict.width(1)
pict.goto(-200, 200)
pict.right(90)
pict.pendown()
pict.turtlesize(0.1)


def left():
    pict.setheading(180)
    pict.forward(step_size)


def right():
    pict.setheading(0)
    pict.forward(step_size)


def up():
    pict.setheading(90)
    pict.forward(step_size)


def down():
    pict.setheading(270)
    pict.forward(step_size)


def increase_step():
    global step_size
    step_size += 10


def decrease_step():
    global step_size
    step_size -= 10
    if step_size < 1:
        step_size = 1


turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(increase_step, '8')
turtle.onkey(decrease_step, '2')

'''
Make this the last part of the code!
'''
my_screen = turtle.Screen()
my_screen.exitonclick()