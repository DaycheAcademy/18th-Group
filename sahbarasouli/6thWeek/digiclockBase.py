import time
import datetime
import turtle 

clock=turtle.Turtle(visible=False)

turtle.color('blue')
turtle.tracer(2,50)
while(True) :
    turtle.clear()
    turtle.write(datetime.datetime.now().strftime('%H' '\t' '%M''\t' '%S'),font=("Arial",30),align="center")
    time.sleep(1)
turtle.done()