from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.moveSpeed=0.1

    def move(self):
        newX=self.xcor()+self.xmove
        newY=self.ycor()+self.ymove
        self.goto(newX,newY)

    def ybounce(self):
        self.ymove*=-1
    def xbounce(self):
        self.xmove *= -1
        self.moveSpeed*=0.75

    def reset_pos(self):
        self.goto(0,0)
        self.xbounce()
        self.moveSpeed=0.1