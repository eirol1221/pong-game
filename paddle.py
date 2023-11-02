from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.shapesize(5.0, 1.0)
        self.goto(position)

    def go_up(self):
        paddle_x = self.xcor()
        paddle_y = self.ycor()
        self.goto(paddle_x, paddle_y + 20)

    def go_down(self):
        paddle_x = self.xcor()
        paddle_y = self.ycor()
        self.goto(paddle_x, paddle_y - 20)
