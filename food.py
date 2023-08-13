from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(0.6,0.6)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))