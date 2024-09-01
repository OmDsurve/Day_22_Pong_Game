from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((475, 0))
l_paddle = Paddle((-485, 0))





screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:

    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -275:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 448 or ball.distance(l_paddle) < 50 and ball.xcor() < -450:
        ball.bounce_x()

    # Detect that right paddle misses the ball
    if ball.xcor() > 490:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -495:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()