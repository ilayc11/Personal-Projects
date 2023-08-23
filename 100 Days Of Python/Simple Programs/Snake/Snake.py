from turtle import Turtle,Screen
STARTPOS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in STARTPOS:
            self.addSeg(pos)

    def extend(self):
        self.addSeg(self.segments[-1].position())

    def addSeg(self,position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != RIGHT:
         self.segments[0].setheading(180)
