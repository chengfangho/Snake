from turtle import Turtle, Screen

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)
            
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
       
    def move(self):
        for segment_pos in range(len(self.segments)-1, 0, -1):
            segment_x = self.segments[segment_pos-1].xcor()
            segment_y = self.segments[segment_pos-1].ycor()
            self.segments[segment_pos].goto(segment_x, segment_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def reset(self):
        for segment in self.segments:
           segment.goto(1000,1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)