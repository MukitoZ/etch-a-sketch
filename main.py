from turtle import Turtle, Screen

zack = Turtle()
screen = Screen()


def move_forward():
    zack.forward(10)


def move_backward():
    zack.backward(10)


def turn_left():
    new_heading = zack.heading() + 10
    zack.setheading(new_heading)


def turn_right():
    new_heading = zack.heading() - 10
    zack.setheading(new_heading)


def clear():
    zack.clear()
    zack.penup()
    zack.home()
    zack.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
