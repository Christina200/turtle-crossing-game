COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from hashlib import new
import random
from turtle import Turtle
class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
    def generate_car(self):
        new_color = random.choice(COLORS)
        new_y = random.randrange(start=-250, stop=250, step=30)
        new_car = Turtle()
        new_car.pu()
        new_car.goto(x=290, y=new_y)
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(new_color)
        new_car.setheading(180)
        new_car.speed("fastest")
        self.cars.append(new_car)
    def move_car(self):
        for car in self.cars:
            car.fd(self.speed)
    def speed_up(self):
        self.speed += MOVE_INCREMENT