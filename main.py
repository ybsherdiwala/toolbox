import turtle
import random

try:
    screen = turtle.Screen()
    screen.screensize(500, 500)
    screen.title("Random Squares")
    screen.bgcolor("blue")

    colors = ["green", "red", "yellow", "purple", "turquoise", "gold", "cyan", "deep pink"]

    turtle.speed(10)

    def square():
        size = random.randint(20, 50)
        x = random.randint(-250+size, 250-size)
        y = random.randint(-250+size, 250-size)
        color = random.choice(colors)

        turtle.fillcolor(color)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(0)

        turtle.begin_fill()
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.end_fill()

        #reset()

    for i in range(30):
        square()

    screen.mainloop()
except turtle.Terminator:
    pass