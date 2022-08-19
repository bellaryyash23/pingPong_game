from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
r_paddle = Paddle(x_pos=350)
l_paddle = Paddle(x_pos=-350)
ball = Ball()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 55 and ball.xcor() > 320) or (ball.distance(l_paddle) < 55 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect miss by r_paddle
    if ball.xcor() > 375:
        scoreboard.l_point()
        ball.restart()

    # Detect miss by l_paddle
    if ball.xcor() < -375:
        scoreboard.r_point()
        ball.restart()

    if scoreboard.r_score == 5 or scoreboard.l_score == 5:
        scoreboard.game_over()
        game_on = False


screen.exitonclick()
