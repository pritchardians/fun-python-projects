SCREEN_WIDTH = 450
ETCH_A_SKETCH_WIDTH = SCREEN_WIDTH + 50
SCREEN_HEIGHT = 250
ETCH_A_SKETCH_HEIGHT = SCREEN_HEIGHT + 100
OUTER_CIRCLE = 50
INNER_CIRCLE = 25
QUARTER_CIRCLE = 90


def inner_screen(pic):
    pic.penup()
    pic.goto(-230, -40)
    pic.down()
    pic.forward(SCREEN_WIDTH)
    pic.circle(INNER_CIRCLE, QUARTER_CIRCLE)
    pic.forward(SCREEN_HEIGHT)
    pic.circle(INNER_CIRCLE, QUARTER_CIRCLE)
    pic.forward(SCREEN_WIDTH)
    pic.circle(INNER_CIRCLE, QUARTER_CIRCLE)
    pic.forward(SCREEN_HEIGHT)
    pic.circle(INNER_CIRCLE, QUARTER_CIRCLE)


def outer_edge(pic):
    pic.penup()
    pic.goto(-250, -150)
    pic.pendown()
    pic.width(5)
    pic.forward(ETCH_A_SKETCH_WIDTH)
    pic.circle(OUTER_CIRCLE, QUARTER_CIRCLE)
    pic.forward(ETCH_A_SKETCH_HEIGHT)
    pic.circle(OUTER_CIRCLE, QUARTER_CIRCLE)
    pic.forward(ETCH_A_SKETCH_WIDTH)
    pic.circle(OUTER_CIRCLE, QUARTER_CIRCLE)
    pic.forward(ETCH_A_SKETCH_HEIGHT)
    pic.circle(OUTER_CIRCLE, QUARTER_CIRCLE)


def knobs(pic):
    pic.penup()
    pic.goto(-250, -140)
    pic.pendown()
    pic.color('gray')
    pic.width(4)
    pic.circle(35)
    pic.penup()
    pic.forward(SCREEN_WIDTH + 50)
    pic.pendown()
    pic.circle(35)


def letters(pic):
    pic.penup()
    pic.left(180)
    pic.forward(250)
    pic.right(90)
    pic.forward(25)
    pic.pendown()
    pic.color('blue')
    style = ('Arial', 30, 'bold italic')
    pic.write('Etch A Sketch', font=style, align='center')

def cursor_start_position(pic):
    pic.penup()
    pic.color('black')
    pic.width(1)
    pic.goto(-200, 200)
    pic.right(90)
    pic.pendown()
    pic.turtlesize(0.1)
