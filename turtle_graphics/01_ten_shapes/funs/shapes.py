import random


def random_colour():
    red = random.randint(0, 100) / 100
    blue = random.randint(0, 100) / 100
    green = random.randint(0, 100) / 100
    return (red, blue, green)


def draw_shape(pic, sides):
    pic.speed(sides)
    pic.width(sides * 2)
    pic.color(random_colour())
    degrees_to_turn = 360 / sides
    for _ in range(1, sides + 1):
        pic.left(degrees_to_turn)
        pic.forward(100)
