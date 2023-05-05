from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.move, "Up")
car = CarManager()
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.go()

    for car_item in car.all_cars:
        if player.distance(car_item) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car.new_level()
        score.level_up()


screen.exitonclick()