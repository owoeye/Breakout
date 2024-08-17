from turtle import Turtle

# MOVE = 0.01
MOVE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_dist = MOVE
        self.y_dist = MOVE
        self.reset()

    def move(self):
        # move the ball with a speed of 10
        new_y = self.ycor() + self.y_dist
        new_x = self.xcor() + self.x_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            # reverse direction of motion in x axis
            self.x_dist *= -1
        if y_bounce:
            # reverse direction of motion on the y axis
            self.y_dist *= -1

    def reset(self):
        # reset ball to origin on top of the paddle
        # self.goto(x=0, y=-220)
        self.goto(x=0, y=-230)
        self.y_dist = 10  # displace ball position so it shoots out at an angle

