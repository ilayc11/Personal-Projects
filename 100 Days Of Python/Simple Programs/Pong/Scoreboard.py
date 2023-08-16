from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier",80,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore=0
        self.rScore=0
        self.updateScoreboard()


    def updateScoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lScore, align=ALIGMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.rScore, align=ALIGMENT, font=FONT)

    def lPoint(self):
        self.lScore+=1
        self.updateScoreboard()

    def rPoint(self):
        self.rScore+=1
        self.updateScoreboard()