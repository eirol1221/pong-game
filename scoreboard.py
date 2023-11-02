from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        # self.center_line()
        self.up()
        self.hideturtle()
        self.goto(0, 260)

        # def center_line(self):
        #     self.up()
        #     self.goto(0, -300)
        #     self.setheading(90)
        #     while self.ycor() < 260:
        #         self.down()
        #         self.forward(20)
        #         self.up()
        #         self.forward(20)

    def show_score(self):
        self.clear()
        self.write(f"{self.left_score} | {self.right_score}",
                   False,
                   "center",
                   ("Arial", 24, "normal"))
