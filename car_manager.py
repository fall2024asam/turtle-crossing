from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.ycor = random.randrange(-250,290,5)
        self.goto(300,self.ycor)
        self.setheading(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
