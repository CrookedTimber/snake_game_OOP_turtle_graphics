from turtle import Turtle
from settings import HEIGHT, WIDTH, FOOD_COLOR
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_location = random.randint(-(WIDTH / 2 - 20), (WIDTH / 2 - 20))
        y_location = random.randint(-(HEIGHT / 2 - 20), (HEIGHT / 2 - 20))
        self.goto(x_location, y_location)
