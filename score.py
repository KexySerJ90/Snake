from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point=0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.write(f'SCORE: {self.point}', align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game over!', align='center', font=('Arial', 20, 'normal'))
    def win(self):
        self.point+=1
        self.clear()
        self.update_score()

