# tahta her iki kenardaki kaleler. Bot olan tahta y koordinatı bakımından topla olan mesafesine göre hareket edecek.

from turtle import Turtle





class Tahta(Turtle):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(x, 0)

    def yukari_cik(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def asagi_in(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)