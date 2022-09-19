from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=700, height=400)
user_bet = screen.textinput(title="Make your bate",
                            prompt="which turtle is win the race ?? Enter the color('red', 'orange', 'yellow', 'green', 'blue', 'purple'): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-75, -45, -15, 15, 45, 75]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.color()
    new_turtle.penup()
    new_turtle.goto(x=-330, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 310:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you Win! the {winning_color} turtle is win!!!!")
            else:
                print(f"you loos! the {winning_color} turtle is win!!!!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
