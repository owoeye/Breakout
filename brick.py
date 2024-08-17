from turtle import Turtle
import random

COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']


# create class for each brick
class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(random.choice(COLOR_LIST))
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.goto(x=x_cor, y=y_cor)

        # # Defining borders of the brick
        self.left_wall = self.xcor() - 50
        self.right_wall = self.xcor() + 50
        self.top_wall = self.ycor() + 20
        self.bottom_wall = self.ycor() - 20


# create a class for layering the bricks
class Bricks:
    def __init__(self):
        self.y_start = 44
        self.y_end = 240
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-446, 500, 104):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 44):
            self.create_lane(i)

