import turtle

try:

    screen = turtle.Screen()
    screen.screensize(500, 500)
    screen.title("Turtle Picture")
    screen.bgcolor("yellow")

    turtle.speed(0)

    def shape():
        for i in range(12):
            turtle.left(30)
            turtle.forward(20)
            turtle.left(30)
            turtle.forward(20)
            turtle.right(30)
            turtle.forward(20)

    for i in range(6):
        turtle.pencolor("red")
        turtle.right(20)
        shape()
        turtle.pencolor("green")
        turtle.right(20)
        shape()
        turtle.pencolor("blue")
        turtle.right(20)
        shape()

    screen.mainloop()
except turtle.Terminator:
    pass