# Try to increase the turtle speed.


import time
from turtle import Screen
from player import Player
from levels import Levels
from car_manager import CarManager
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle-Crossing")
screen.tracer(0)

player = Player()
levels = Levels()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up,'Up')

game_is_on = True
while game_is_on:
    time.sleep(player.player_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detecting collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            levels.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        levels.increase_level()


screen.exitonclick()



