import turtle

# Set up the Turtle
turtle.speed(12)
turtle.hideturtle()
turtle.penup()
turtle.goto(-200, 200)  # Starting position for drawing the grid

# Draw outer square with pensize 5
turtle.pensize(5)
for _ in range(4):
    turtle.pendown()
    turtle.forward(450)
    turtle.right(90)
    turtle.penup()

# Draw Vertical Lines pensize 3 and 1
for i in range(1, 9):
    if not (i % 3):
        turtle.pensize(3)
    else:
        turtle.pensize(1)
    turtle.goto(-200 + (i * 50), 200)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(450)
    turtle.left(90)
    turtle.penup()

# Draw horizontal Lines pensize 3 and 1
for j in range(1, 9):
    if not (j % 3):
        turtle.pensize(3)
    else:
        turtle.pensize(1)
    turtle.goto(-200, 200 - (j * 50))
    turtle.pendown()
    turtle.forward(450)
    turtle.penup()


turtle.done()
