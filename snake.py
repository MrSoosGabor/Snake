import turtle
import time


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(jobbra, "Right")
palya.onkey(balra, "Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

kijelzo = turtle.Turtle()
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.sety(240)

while True:
    fej.forward(20)

    if fej.xcor() < -400 or fej.xcor() > 400 or fej.ycor() < -300 or fej.ycor() > 300:
        kijelzo.clear()
        kijelzo.write("Megdöglött a kukac", align="center", font=("Ariel", 36, "bold"))
    palya.update()
    time.sleep(0.3)
