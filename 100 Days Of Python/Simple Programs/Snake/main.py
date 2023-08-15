from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb=Scoreboard()
gameSpeed=0.1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameActive = True
while gameActive:
    screen.update()
    time.sleep(gameSpeed)
    snake.move()

    if snake.head.distance(food) < 18:
        gameSpeed-=0.005
        food.refresh()
        snake.extend()
        sb.increaseScore()

    if snake.head.xcor()>280 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-280:
        gameActive=False
        sb.gameOver()

    for seg in snake.segments:
        if seg == snake.head:
            continue
        if snake.head.distance(seg)<18:
            gameActive=False
            sb.gameOver()

screen.exitonclick()
