from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # создаем список начальных позиций для сегментов змеи
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # создаем сегменты змеи и добавляем их в список
        for pos in STARTING_POS:
            self.add_seg(pos)

    def add_seg(self, pos):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):

        # 1. Начинаем цикл, который проходит по всем сегментам змеи, кроме головы (от последнего до второго)
        for seg in range(len(self.segments) - 1, 0, -1):
            # 2. Получаем координаты сегмента перед текущим сегментом и сохраняем их в переменные new_x и new_y
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            # 3. Перемещаем текущий сегмент на новые координаты (new_x, new_y)
            self.segments[seg].goto(new_x, new_y)

        # двигаем голову змеи вперед на 20 пикселей
        self.head.forward(MOVE_DIST)

    def up(self):
        # Проверка текущего направления головы змеи
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]