from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_to_start()
        self.setheading(90)     # Turtle faces North
        self.player_speed = 0.1

    def go_up(self):
        self.forward(MOVE_DISTANCE)        # Want Turtle to run faster? Edit MOVE_DISTANCE above


    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        # self.player_speed *= 0.9
