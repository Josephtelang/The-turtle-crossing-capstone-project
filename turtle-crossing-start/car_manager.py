from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        
        self.cars_list = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 or random_chance == 2:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_y = random.randint(-250,250)
            new_car.goto(290,new_y)
            new_car.setheading(180)
            self.cars_list.append(new_car)
        
        
    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.cars_speed)
            
    def Level_up(self):
        self.cars_speed += MOVE_INCREMENT
        
      
