import time
import random
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#Create objects
turtle = Player()
cars = []
scoreboard = Scoreboard()
scoreboard.print_level()

#Listen for "up" key to move turtle
screen.listen()
screen.onkey(turtle.move, "Up")

#Create variables to adjust time.sleep (speed of cars) and throttle car generation
speed = 0.1
iteration_count = 0

#Run main game
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    #Create cars
    # for _ in range(random.randint(0, 3)):
    if iteration_count ==8:
        car = CarManager()
        cars.append(car)
        iteration_count = 0

    #Loop through cars list and move each one
    for car in cars:
        car.move()

    #Detect collision
    for car in cars:
        if turtle.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    #test if turtle has reach other side of road and if so, reset to original position
    if turtle.ycor() > 290:
        turtle.reset()
        speed = speed * 0.7
        scoreboard.increase_score()
        scoreboard.print_level()

    for i in range(0,len(cars)-1):
        if cars[i].xcor() < -300:
            cars[i].hideturtle()
            cars.pop(i)

    # increment iteration_count
    iteration_count += 1

    print(speed)
    print(len(cars))

screen.exitonclick()