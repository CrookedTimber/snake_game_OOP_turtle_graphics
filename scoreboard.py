from turtle import Turtle

from settings import HEIGHT


ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("01 snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, HEIGHT / 2 - 100)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(
    #         f"GAME OVER",
    #         align=ALIGNMENT,
    #         font=FONT,
    #     )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()
