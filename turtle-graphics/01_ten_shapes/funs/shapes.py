import random


def random_colour(pic):
    c_red = random.randint(0, 100) / 100
    c_green = random.randint(0, 100) / 100
    c_blue = random.randint(0, 100) / 100
    pic.color(c_red, c_green, c_blue)


def draw_shape(pic, sides):
    pic.speed(sides)
    pic.width(sides * 2)
    random_colour(pic)
    degrees_to_turn = 360 / sides
    for _ in range(1, sides + 1):
        pic.left(degrees_to_turn)
        pic.forward(100)
