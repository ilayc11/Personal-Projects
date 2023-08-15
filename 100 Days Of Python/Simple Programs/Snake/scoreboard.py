from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier",24,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)


    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()
