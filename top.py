from turtle import Turtle
import random

class Top(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def hareket_et(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def çarpma_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    def carpma_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.home()
        self.x_move *= -1
        self.move_speed = 0.1

