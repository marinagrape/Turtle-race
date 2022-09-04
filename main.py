from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color!")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(tim)

if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You won! The {win_color} turle is the champ!")
            else:
                print(f"You lost :( The {win_color} turtle won!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()

