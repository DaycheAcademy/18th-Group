import time
import turtle

TehranTime = time.localtime()
t1 = turtle.Turtle()      # draw a Box for covering
t2 = turtle.Turtle()      # write time in Box
t3 = turtle.Turtle()      # write date in Box
screen = turtle.Screen()
screen.bgcolor("silver")
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
# --------------------------
t1.penup()
t2.penup()
t3.penup()
t1.goto(-300, 200)
t1.speed(12)
t1.pensize(6)
for _ in range(2):
    t1.pendown()
    t1.forward(600)
    t1.right(90)
    t1.forward(450)
    t1.right(90)
t1.penup()

# ------------------------
t2.goto(0, -50)
t2.speed(10)
t2.pendown()
t2.write('{} : {} : {}' .format(TehranTime.tm_hour, TehranTime.tm_min, TehranTime.tm_sec),
                          move=False, align='Center', font=('Arial', 80, 'normal'))

# -------------------------
t3.goto(0, -100)
t3.speed(10)
t3.pendown()
t3.write('{}  -  {}  -  {}' .format(TehranTime.tm_year, TehranTime.tm_mon, TehranTime.tm_mday),
                          move=False, align='Center', font=('Times New Roman', 20, 'normal'))
turtle.done()
