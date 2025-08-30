from turtle import Turtle,Screen
import random
game_on=False
screen=Screen()
screen.setup(width=800,height=600)
user_bet=screen.textinput(title="Make a bet",prompt="Enter your choice of turtle")
color=['red','orange','yellow','green','blue','purple']
y_cor=[-250,-150,-50,50,150,250]
all_turtle=[]



for turtle_index in range(0,6):
    t = Turtle(shape="turtle")
    t.color(color[turtle_index])
    t.teleport(x=-350,y=y_cor[turtle_index])
    all_turtle.append(t)

if user_bet:
    game_on=True



while game_on :
    for turtle in all_turtle:
        if turtle.xcor()>=350:
            color=turtle.color()
            if color[0]==user_bet:
                print(f"You won the bet!! {color[0]} won the race.")
            else:
                print(f"You lost the bet!! {color[0]} won the race")

            game_on=False
            break

    for i in range(0,6):
        all_turtle[i].forward(random.randint(1,10))

screen.exitonclick()