from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as score:
            self.high_score = int(score.read())
        self.score = 0
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}                                          High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as score:
                score.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
