from turtle import Screen, up, down
from Intermediate_codes.pong_game.paddle import Paddle
from Intermediate_codes.pong_game.ball import Ball
from Intermediate_codes.pong_game.scoreboard import ScoreBoard

LEFT = (-350, 0)
RIGHT = (350, 0)

screen = Screen()
l_paddle = Paddle(LEFT)
r_paddle = Paddle(RIGHT)
ball = Ball()
score = ScoreBoard()

screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")


screen.listen()
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()
