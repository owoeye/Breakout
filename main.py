import turtle as tr
from paddle import Paddle
from ball import Ball
from brick import Bricks
from score import Score, GameOver
import time

# create window
window = tr.Screen()
window.setup(width=1000, height=600)
window.bgcolor("black")
window.title("Breakout")
window.tracer(0)  # turn off animation

# create paddle
paddle = Paddle()
# create ball
ball = Ball()
# create bricks
bricks = Bricks()
# create score board
score = Score()
# game over text
gameOver = GameOver()

# move paddle with key strokes
window.listen()
window.onkey(key="Left", fun=paddle.move_left)
window.onkey(key="Right", fun=paddle.move_right)

game_on = True
while game_on:
    window.update()  # show turtles(paddle and ball) on window
    time.sleep(0.02)
    ball.move()

    # collision with walls
    # detect collision with left and right of wall
    if ball.xcor() < -500 or ball.xcor() > 500:
        ball.bounce(x_bounce=True, y_bounce=False)

    # detect collision with top of wall
    if ball.ycor() > 300:
        ball.bounce(x_bounce=False, y_bounce=True)

    # detect collision with bottom of wall
    if ball.ycor() < -300:
        ball.reset()
        score.decrease_lives()

    # ball collision with paddle
    if ball.distance(paddle) < 110 and ball.ycor() < -220:
        # left of paddle                  right of paddle
        if ball.xcor() < paddle.xcor() or ball.xcor() > paddle.xcor():
            ball.bounce(x_bounce=False, y_bounce=True)
        # middle of paddle
        else:
            ball.bounce(x_bounce=True, y_bounce=True)

    # collision with a brick
    for brick in bricks.bricks:
        if ball.distance(brick) < 65:
            # to detect collision with brick
            # from left side or right side
            if ball.xcor() < brick.left_wall or ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            # from top or bottom
            elif ball.ycor() < brick.top_wall or ball.ycor() > brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            brick.hideturtle()  # deletes drawing from on screen
            score.increase_score()
            bricks.bricks.remove(brick)

    # show end game
    no_bricks = bricks.bricks
    no_lives = score.lives
    if no_lives == 0 or len(no_bricks) == 0:
        gameOver.is_game_over(no_bricks, no_lives)
        time.sleep(3)
        # Reset game
        score.reset()  # reset score numbers back to default
        gameOver.clear()  # remove game over message
        bricks.create_all_lanes()  # recreate all bricks

tr.mainloop()
