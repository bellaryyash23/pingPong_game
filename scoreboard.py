from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        if self.l_score >= 5:
            self.write("LEFT WON!", align="center", font=("Courier", 50, "bold"))
        elif self.r_score >= 5:
            self.write("RIGHT WON!", align="center", font=("Courier", 50, "bold"))

    # def line(self):
    #     self.goto(0, 300)
    #     self.setheading(270)
    #     while self.ycor() > -300:
    #         self.pendown()
    #         self.forward(20)
    #         self.penup()
