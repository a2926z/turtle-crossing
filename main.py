from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from pygame import mixer



mixer.init()

FINISH_LINE_Y = 275

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
score.lifes()
score.high_score()


car = CarManager()
car.lane_generator()
car.gate_generator()

screen.listen()
screen.onkey(player.move_player, 'Up')
screen.onkey(player.move_backwar, 'Down')

game_is_on = True

def play():
    global game_is_on
    while game_is_on:
        sleep(0.1)
        screen.update()
        car.generate_car()
        car.move_car()

        if player.ycor() > FINISH_LINE_Y:
            player.finish_line()
            score.update_level()
            score.high_score()
            # score.gain_life()
            car.increase_car_speed()
            mixer.music.load('crossed.mp3')
            mixer.music.play()


        for i in car.all_cars:
            if player.distance(i) < 30:
                # print('crashhhhhhhhhhhhhhhhhhhhhh')
                player.car_collision()
                mixer.Channel(2).play(mixer.Sound('smb_touch.wav'))
                score.lives_update()

                if score.lives == 0:
                    game_is_on = False
                    score.game_over()
                    score.get_highscore()
                    if score.level > score.highscore_level:
                        with open('high_score.txt', 'w') as f:
                            f.write(str(score.level))
                    mixer.Channel(3).play(mixer.Sound('game_over.wav'))


            if i.xcor() < -320:
                car.all_cars.remove(i)
                i.hideturtle()
            if len(car.all_cars) < 12:
                car.generate_car()
        # print(len(car.all_cars))

def exita():
    global game_is_on
    game_is_on = False

screen.onkey(exita, 'q')

play()
screen.exitonclick()