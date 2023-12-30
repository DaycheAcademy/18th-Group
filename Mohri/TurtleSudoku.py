import turtle

turtle.speed(0)
turtle.hideturtle()

for i in range(10):
    if i % 3 == 0:
        turtle.pensize(3)
    else:
        turtle.pensize(1)
    turtle.penup()
    turtle.goto(-220, 220 - i * 50)
    turtle.pendown()
    turtle.forward(450)
    turtle.right(90)
    turtle.penup()
    turtle.goto(-220 + i * 50, 220)
    turtle.pendown()
    turtle.forward(450)
    turtle.penup()
    turtle.left(90)
turtle.exitonclick()