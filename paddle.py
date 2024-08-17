from turtle import Turtle

MOVE = 80  # movement speed of paddle


class Paddle(Turtle):
    def __init__(self):
        # define parameters for making the paddle
        super().__init__()  # creating a child class
        self.color("pink")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-250)

    def move_left(self):
        if self.xcor() > -350:
            self.backward(MOVE)

    def move_right(self):
        if self.xcor() < 350:
            self.forward(MOVE)

