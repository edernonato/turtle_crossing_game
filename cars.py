from turtle import Turtle, colormode
from random import randint

colormode(255)


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setheading(180)
        self.x = 0
        self.y = 0
        self.random_position()
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))

    def move_car(self):
        self.forward(5)

    def random_position(self):
        self.y = randint(-250, 250)
        self.setpos(300, self.y)
