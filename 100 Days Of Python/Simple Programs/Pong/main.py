import time
from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rPaddle = Paddle((350, 0))
lPaddle = Paddle((-350, 0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(rPaddle.go_up, "Up")
screen.onkey(rPaddle.go_down, "Down")
screen.onkey(lPaddle.go_up, "w")
screen.onkey(lPaddle.go_down, "s")

gameActive = True
while gameActive:
    screen.update()
    ball.move()
    time.sleep(ball.moveSpeed)

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.ybounce()

    if ball.distance(rPaddle)<50 and ball.xcor()>320 or ball.distance(lPaddle)<50 and ball.xcor()<-320:
        ball.xbounce()

    if ball.xcor()>380:
        ball.reset_pos()
        scoreboard.lPoint()

    if ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.rPoint()

screen.exitonclick()
