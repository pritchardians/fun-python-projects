def left(pic, step_size):
    pic.setheading(180)
    pic.forward(step_size)


def right(pic, step_size):
    pic.setheading(0)
    pic.forward(step_size)


def up(pic, step_size):
    pic.setheading(90)
    pic.forward(step_size)


def down(pic, step_size):
    pic.setheading(270)
    pic.forward(step_size)


def increase_step_size(pic, step_size):
    step_size += 10
    if step_size > 50:
        step_size = 50
    return step_size


def decrease_step_size(pic, step_size):
    step_size -= 10
    if step_size < 1:
        step_size = 1
    return step_size
