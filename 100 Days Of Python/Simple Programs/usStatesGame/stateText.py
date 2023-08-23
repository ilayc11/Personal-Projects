from turtle import Turtle
class stateText(Turtle):
    def __init__(self,name,x,y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.write(name)