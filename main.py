import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

GENERATE_INTERVAL = 5
FINISH_LINE_Y = 270

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move,key="Up")

game_is_on = True
generate_helper = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # generate car flows
    if (generate_helper % GENERATE_INTERVAL) == 0:
        car_manager.generate_car()
        car_manager.move_car()
    generate_helper += 1
    # detect the collsion between the turtle and cars
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
    # detect if the turtle reaches the final line. If so, send it back to start point and speed cars up.
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_pos()
        car_manager.speed_up()
        scoreboard.inc_level()

screen.exitonclick()
