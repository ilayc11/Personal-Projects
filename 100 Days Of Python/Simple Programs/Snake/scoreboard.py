from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier",24,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            file=open("highscore.txt",'x')
            file.write("0")
            file.close()
            file=open("highscore.txt",'r')
        except FileExistsError:
            file=open("highscore.txt",'r')
        finally:
            self.highScore = int(file.read())
            file.close()

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        file = open("highscore.txt", 'r')
        self.write(f"Score: {self.score} High Score: {file.read()}", align=ALIGMENT, font=FONT)
        file.close()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            file=open("highscore.txt",'w')
            file.write(str(self.highScore))
            file.close()


        self.score = 0
        self.updateScoreBoard()

    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()
