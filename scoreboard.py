from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.color("black")
        self.setpos(-250, 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Center", font=("Arial", 15, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="Center", font=("Arial", 15, "normal"))