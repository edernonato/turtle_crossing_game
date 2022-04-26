from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.turtlesize(1)
        self.shape("turtle")
        self.setheading(90)
        self.refresh()

    def move(self):
        self.forward(10)

    def refresh(self):
        self.goto(0, -280)

    def is_at_finish_line(self):
        if self.ycor() >= 300:
            self.refresh()
            return True
        else:
            return False
