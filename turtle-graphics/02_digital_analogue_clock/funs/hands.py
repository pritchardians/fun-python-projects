def hand_setup(pic):
    pic.penup()
    pic.setpos(0, 0)
    pic.setheading(90)


def draw_hour_hand(pic, time_in):
    pic.width(6)
    hand_setup(pic)
    pic.right(time_in.hour * 30)
    pic.pendown()
    pic.forward(100)


def render_hour_hand(pic, time_in):
    pic.color('slategray')
    draw_hour_hand(pic, time_in)


def delete_hour_hand(pic, time_in):
    pic.color('white')
    draw_hour_hand(pic, time_in)


def draw_minute_hand(pic, time_in):
    pic.width(8)
    hand_setup(pic)
    pic.right(time_in.minute * 6)
    pic.pendown()
    pic.forward(150)


def render_minute_hand(pic, time_in):
    pic.color('gray')
    draw_minute_hand(pic, time_in)


def delete_minute_hand(pic, time_in):
    pic.color('white')
    draw_minute_hand(pic, time_in)


def draw_second_hand(pic, time_in):
    pic.penup()
    pic.shape('triangle')
    pic.width(15)
    pic.setpos(0, 0)
    pic.setheading(90)
    pic.right(time_in.second * 6)
    pic.forward(217)
    pic.pendown()
    pic.forward(10)


def render_second_hand(pic, time_in):
    pic.color('red')
    draw_second_hand(pic, time_in)


# Second Hand
def delete_second_hand(pic, time_in):
    pic.color('white')
    draw_second_hand(pic, time_in)
