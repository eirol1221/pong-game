from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG = "black"
TITLE = "The Pong Game"
BALL_X = 200
BALL_Y = 350

screen = Screen()
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
line = Line()

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BG)
screen.title(TITLE)

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True
score.show_score()

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # collision with the paddle
    if ((ball.xcor() > 330 and ball.distance(right_paddle) < 50)
            or (ball.xcor() < -330 and ball.distance(left_paddle) < 50)):
        ball.paddle_bounce()

    # update score
    if ball.xcor() > 390:
        score.left_score += 1
        score.show_score()
        ball.refresh()
    elif ball.xcor() < -390:
        score.right_score += 1
        score.show_score()
        ball.refresh()



screen.exitonclick()