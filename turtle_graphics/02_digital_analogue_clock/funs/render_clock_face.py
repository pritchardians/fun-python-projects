

def render_clock_circles(pic):
    pic.penup()
    pic.setpos(0, -200)
    pic.width(10)
    pic.color('seagreen')
    pic.pendown()
    pic.circle(200)
    pic.penup()
    pic.setpos(0, -240)
    pic.width(3)
    pic.pendown()
    pic.circle(240)
    # style = ('Arial', 30, 'bold italic')

# Ticks
def render_tick_marks(pic):
    for tick in range(0, 12):
        pic.color('lightblue')
        pic.width(3)
        pic.penup()
        pic.setpos(0, 0)
        pic.right(30)
        pic.forward(178)
        pic.pendown()
        pic.forward(15)
        if tick % 3 == 2:
            # Major ticks at 3, 6, 9, 12
            pic.left(180)
            pic.color('navy')
            pic.width(5)
            pic.forward(25)
            pic.penup()
            pic.left(180)
            pic.forward(25)