import time
import datetime
import turtle 

clock=turtle.Turtle(visible=False)
clock.color('blue')
while(True) :
    clock.clear()
    clock.write(datetime.datetime.now().strftime('%H' '\t' '%M''\t' '%S'),font=("Arial",30),align="center")
    time.sleep(1)
turtle.done()