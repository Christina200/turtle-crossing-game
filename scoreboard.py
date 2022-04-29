FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.goto(-200, 250)
        self.hideturtle()
        self.update_level()
    def inc_level(self):
        self.level += 1
        self.update_level()
    def update_level(self):
        self.clear()
        self.write(arg=f"Level {self.level}",align="center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
