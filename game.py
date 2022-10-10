from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from settings import SPEED, WIDTH, HEIGHT
import time

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

player = Snake()
score = Scoreboard()
apple = Food()

screen.listen()
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)
screen.onkey(key="Left", fun=player.left)
screen.onkey(key="Right", fun=player.right)

game_on = True

while game_on:
    screen.update()
    time.sleep(SPEED)
    player.move()

    if player.head.distance(apple) < 15:
        apple.refresh()
        player.extend()
        score.increase_score()

    if (
        player.head.xcor() > (WIDTH / 2 - 10)
        or player.head.xcor() < -(WIDTH / 2 - 10)
        or player.head.ycor() > (HEIGHT / 2 - 10)
        or player.head.ycor() < -(HEIGHT / 2 - 10)
    ):
        score.reset()
        apple.refresh()
        player.reset()

    for segment in player.segments[1:]:
        if player.head.distance(segment) < 10:
            score.reset()
            apple.refresh()
            player.reset()

screen.exitonclick()
