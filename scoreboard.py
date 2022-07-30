from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)

        self.color("white")

        self.score = 0

        self.update_scoreboard()

        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def score_update(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)







