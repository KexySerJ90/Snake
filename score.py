from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open ('data.txt') as f:
            self.high_score=int(f.read())
        self.point=0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f'SCORE: {self.point} High Score: {self.high_score}', align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.point>self.high_score:
            self.high_score=self.point
            with open('data.txt', 'w') as f:
                f.write(f'{self.high_score}')
            self.point=0
            self.update_score()

    def win(self):
        self.point+=1
        self.update_score()

