from turtle import Turtle
from pygame import mixer

STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 15

mixer.init()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)

        self.setheading(90)

    def move_player(self):
        self.forward(MOVE_DISTANCE)
        mixer.Channel(0).play(mixer.Sound('luigirun.wav'))

    def move_backwar(self):
        self.backward(MOVE_DISTANCE)
        mixer.Channel(1).play(mixer.Sound('smb_stomp.wav'))

    def finish_line(self):
        self.goto(STARTING_POSITION)

    def car_collision(self):
        self.goto(STARTING_POSITION)




