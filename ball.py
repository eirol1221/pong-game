from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.speed("slowest")
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.1

    def move(self):
        self.set_position()

    def bounce(self):
        self.move_y *= -1
        self.set_position()

    def paddle_bounce(self):
        self.move_x *= -1
        self.ball_speed *= 0.9
        self.set_position()

    def refresh(self):
        self.home()
        self.move_x *= -1
        self.ball_speed = 0.1
        self.set_position()

    def set_position(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)