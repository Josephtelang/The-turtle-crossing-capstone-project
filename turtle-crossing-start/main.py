import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
new_car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car.create_car()
    new_car.move_cars()
    
    # Detect the collision with the car.
    for car in new_car.cars_list:
        if car.distance(player)< 20:
            game_is_on = False
            scoreboard.game_over()
            
    if player.reached_final_line():
        player.go_to_start()
        new_car.Level_up()
        scoreboard.increase_level()
        
            
    
screen.exitonclick()