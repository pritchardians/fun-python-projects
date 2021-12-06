import turtle

pict = turtle.Turtle()

pict = turtle.Turtle()
pict.speed(10)
pict.shape('circle')
pict.color('red')
pict.width(3)
pict.turtlesize(0.25)

pict.penup()
pict.goto(-230, -40)
pict.down()
pict.forward(450)


'''
Make this the last part of the code!
'''
my_screen = turtle.Screen()
my_screen.exitonclick()
