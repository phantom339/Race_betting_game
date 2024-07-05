from turtle import *
import random

is_race_on=False
screen=Screen()
screen.setup(width=600,height=600)
user_bet=screen.textinput(title="Make Your bet",prompt="Which Turtle would you like to bet on? Give a color:")
colors=["red","blue","green","purple","orange"]
y_position=[100,50,0,-50,-100]
all_turtles=[]
for i in range(0,5):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-250,y=y_position[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on=True
    while is_race_on:
        for j in all_turtles:
            if j.xcor() > 260:
                is_race_on=False
                winning_c=j.pencolor()
                if winning_c == user_bet:
                    print("Congratulations you won the bet")
                else:
                    print(f"You lost! {winning_c} colored turtle won the race")

            ran_dis=random.randint(0,10)
            j.forward(ran_dis)

screen.exitonclick()