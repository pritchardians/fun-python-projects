import turtle
from funs import draw_etch_a_sketch
from funs import move_cursor

pic = turtle.Turtle()
pic.speed(10)
pic.shape('circle')
pic.color('red')
pic.width(3)
pic.turtlesize(0.25)
step_size = 3

draw_etch_a_sketch.inner_screen(pic)
draw_etch_a_sketch.outer_edge(pic)
draw_etch_a_sketch.knobs(pic)
draw_etch_a_sketch.letters(pic)
draw_etch_a_sketch.cursor_start_position(pic)


# Respond to key presses and move cursor / change step size
# Wasn't able to figure out how to move these functions as they are instantly invoked
def left():
    move_cursor.left(pic, step_size)


def right():
    move_cursor.right(pic, step_size)


def up():
    move_cursor.up(pic, step_size)


def down():
    move_cursor.down(pic, step_size)


def increase_step_size():
    global step_size
    step_size = move_cursor.increase_step_size(pic, step_size)


def decrease_step_size():
    global step_size
    step_size = move_cursor.decrease_step_size(pic, step_size)


turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(increase_step_size, '8')
turtle.onkey(decrease_step_size, '2')

'''
Make this the last part of the code!
'''
my_screen = turtle.Screen()
my_screen.exitonclick()
