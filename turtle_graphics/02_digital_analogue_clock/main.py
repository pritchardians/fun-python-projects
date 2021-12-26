import turtle
import time
from datetime import datetime
from funs import render_clock_face
from funs import hands

pic = turtle.Turtle()
pic.speed('fastest')
pic.turtlesize(.01)

# Render clock face
render_clock_face.render_clock_circles(pic)
render_clock_face.render_tick_marks(pic)

new_time = datetime.now()
hands.render_hour_hand(pic, new_time)
hands.render_minute_hand(pic, new_time)
hands.render_second_hand(pic, new_time)

old_time = datetime.now()
time_to_end = time.time() + 65

# Make the hands move!
while time.time() < time_to_end:
    new_time = datetime.now()
    if old_time.second != new_time.second:
        hands.delete_second_hand(pic, old_time)
        hands.render_second_hand(pic, new_time)
        if old_time.hour != new_time.hour:
            hands.delete_hour_hand(pic, old_time)
            hands.render_hour_hand(pic, new_time)
            hands.render_minute_hand(pic, new_time)
        if old_time.minute != new_time.minute:
            hands.delete_minute_hand(pic, old_time)
            hands.render_hour_hand(pic, new_time)
            hands.render_minute_hand(pic, new_time)
        old_time = new_time

'''
This bit goes last
'''
my_screen = turtle.Screen()
my_screen.exitonclick()
