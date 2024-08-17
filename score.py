from turtle import Turtle

try:
    score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
    score = open('highestScore.txt', 'w').write(str(0))
except ValueError:
    score = 0

FONT = ("Courier", 18, "bold")
LIVES = 5


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = score
        self.lives = LIVES
        self.goto(-490, 270)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        # self.goto(-100, 200)
        self.write(f"Score: {self.score} | High Score: {self.highscore} | Lives: {self.lives}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            open('highestScore.txt', 'w').write(str(self.highscore))

        self.clear()
        self.score = 0
        self.lives = LIVES
        self.update_score()


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, -200)
        self.color("white")
        self.penup()
        self.hideturtle()

    def is_game_over(self, no_brick, no_lives):
        if len(no_brick) == 0:
            # show result
            self.write('You Cleared the Game', align='center', font=FONT)

        elif no_lives == 0:
            self.write("Game Over", align='center', font=FONT)

