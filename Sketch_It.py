from turtle import Turtle,Screen
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_clockwise():
    tim.right(10)
def move_counterclockwise():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
tim=Turtle()
screen=Screen()
screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=move_clockwise,key="d")
screen.onkey(fun=move_counterclockwise,key="a")
screen.onkey(fun=clear,key="c")
screen.exitonclick()