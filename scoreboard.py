from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.lives = 5
        self.highscore_level = 0
        self.my_level = Turtle()
        self.my_level.color('white')
        self.my_level.hideturtle()
        self.my_level.penup()
        self.my_level.goto(-280, 260)
        self.my_level.clear()
        self.update_level()

    def update_level(self):
        self.level += 1
        self.my_level.clear()
        self.my_level.write(f'Level {self.level}', font=FONT)

    def lifes(self):
        self.my_lifes = Turtle()
        self.my_lifes.color('white')
        self.my_lifes.hideturtle()
        self.my_lifes.penup()
        self.my_lifes.goto(150, 260)
        # self.my_lifes.clear()
        self.my_lifes.write(f'Lives: {self.lives}', font=FONT)

    def lives_update(self):
        self.lives -= 1
        self.my_lifes.clear()
        self.lifes()

    def game_over(self):
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-150, -20)
        self.write(f'GAME OVER', font=("Courier", 42, "normal"))

    def gain_life(self):
        self.lives += 1
        self.lifes()

    def get_highscore(self):
        with open('high_score.txt', 'r') as f:
            contents = f.readlines()
            self.highscore_level = int(contents[0])
            return self.highscore_level

    def high_score(self):
        global my_high_score
        self.get_highscore()
        self.set_new_highscore()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-285, -271)
        self.clear()
        if self.level == self.highscore_level:
            self.color('cyan2')
            self.write(f'High Score: \n Level {self.highscore_level}', font=("Courier", 14, "normal"))

        else:
            self.write(f'High Score: \n Level {self.highscore_level}', font=("Courier", 14, "normal"))

    def set_new_highscore(self):
        if self.level >= self.highscore_level:
            self.highscore_level = self.level
            self.color('cyan2')
            return self.highscore_level


