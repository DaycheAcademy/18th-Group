import turtle as clock
import time

clock.speed(0)
clock.bgcolor("black")
clock.color("medium sea green")
clock.hideturtle()


def update_time():
   clock.clear()
   clock.write(time.strftime('%H:%M:%S %p'), align='center', font=('Arial', 30, 'bold'))
   clock.ontimer(update_time, 1000)


update_time()

clock.exitonclick()