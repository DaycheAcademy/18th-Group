import turtle
import datetime

tdate = turtle.Turtle()      # write date in Box
screen = turtle.Screen()
screen.bgcolor("silver")
tdate.hideturtle()
tdate.penup()
turtle.tracer(n=1, delay=0)
turtle.hideturtle()
while True:
    turtle.clear()
    currentTime = datetime.datetime.now()
    turtle.goto(0, 0)
    turtle.speed(1)
    turtle.pendown()
    turtle.write(' {} : {} : {} '  .format(currentTime.strftime("%H"), currentTime.strftime("%M"), currentTime.strftime("%S")),
                                                             move=False, align='Center', font=('B titr', 45, 'normal'))
    tdate.goto(0, -100)
    tdate.speed(0)
    tdate.pendown()
    tdate.write('20{}  -  {}  -  {}' .format(currentTime.strftime("%y"), currentTime.strftime("%m"), currentTime.strftime("%d")),
                              move=False, align='Center', font=('B nazanin', 20, 'normal'))

