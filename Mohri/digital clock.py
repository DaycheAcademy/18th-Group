import turtle as clock
import time

clock.hideturtle()
clock.speed(0)
clock.bgcolor("black")
clock.color("white")


def update_time():
   clock.clear()
   clock.write(time.strftime('%H:%M:%S %p'), align='center', font=('Arial', 30, 'bold'))
   clock.ontimer(update_time, 1000)


update_time()

clock.exitonclick()