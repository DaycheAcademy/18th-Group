import turtle
import time
#set first position top left of screen
mySudoku=turtle.Turtle(visible=False)
mySudoku.penup()
mySudoku.setx(-300)
mySudoku.sety(300)
mySudoku.pendown()
mySudoku.speed(0)
#drawing the main rectangle9*9
for rect in range(4):
    mySudoku.pensize(5)
    mySudoku.forward(603)
    mySudoku.right(90)
    
# drawing rectangle 3*3
mySudoku.penup()
mySudoku.setx(-300)
mySudoku.sety(300)

mySudoku.pensize(3)

for i in range(1,3):
    mySudoku.penup()
    mySudoku.setx(-300)
    mySudoku.sety(300)
    mySudoku.pendown()
    mySudoku.forward(201*i)
    mySudoku.right(90)
    mySudoku.forward(603)
    mySudoku.left(90)


for i in range(1,3):
    mySudoku.penup()
    mySudoku.setx(-300)
    mySudoku.sety(300)
    mySudoku.pendown()
    mySudoku.right(90)
    mySudoku.forward(201*i)
    mySudoku.left(90)
    mySudoku.forward(603)

# drawing rectangle 1*1
mySudoku.pensize(1)


for i in range(1,9):
    mySudoku.penup()
    mySudoku.setx(-300)
    mySudoku.sety(300)
    mySudoku.pendown()
    mySudoku.right(90)
    mySudoku.forward(67*i)
    mySudoku.left(90)
    mySudoku.forward(603)

for i in range(1,9):
    mySudoku.penup()
    mySudoku.setx(-300)
    mySudoku.sety(300)
    mySudoku.pendown()
    mySudoku.forward(67*i)
    mySudoku.right(90)
    mySudoku.forward(603)
    mySudoku.left(90)

turtle.done()

