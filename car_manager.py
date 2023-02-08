from turtle import Turtle
from random import choice, randint

COLORS = ["red", "dark orange", "cyan", "green", "dodger blue", "deep sky blue", "yellow", "gold"]
STARTING_MOVE_DISTANCE = 7
MOVE_INCREMENT = 0.7
Y_AXIS = list(range(-250, 260, 40))


class CarManager:

    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        # A way to slow down the generated cars, ## Who could have thought that?????
        random_chance = randint(1, 3)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.goto(300, choice(Y_AXIS))
            self.all_cars.append(new_car)
            # print(self.all_cars)
            # print(Y_AXIS)
            # print(choice(Y_AXIS))

    def move_car(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_car_speed(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        # print(STARTING_MOVE_DISTANCE)

    def lane_generator(self):
        y = -270
        for times in range(14):
            lane = Turtle()
            lane.color('white')
            lane.penup()
            lane.goto(285, y)
            lane.setheading(180)
            y += 40
            for i in range(12):
                lane.pendown()
                lane.forward(40)
                lane.penup()
                lane.forward(10)

    def gate_generator(self):
        gate = Turtle()
        gate.color('white')
        gate.penup()
        gate.goto(-30, 280)
        gate.setheading(90)
        gate.pendown()
        gate.width(6)
        gate.forward(40)
        gate.penup()
        gate.goto(30, 280)
        gate.pendown()
        gate.forward(60)




