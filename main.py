from turtle import Screen, Turtle
import time

# создаем экран
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snack game')
screen.tracer(0)

# создаем список начальных позиций для сегментов змеи
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# создаем сегменты змеи и добавляем их в список
for pos in starting_pos:
    segment = Turtle('square')
    segment.color('white')
    segment.penup()
    segment.goto(pos)
    segments.append(segment)

# запускаем игру
game_is_on = True
while game_is_on:
    # обновляем экран и задерживаем выполнение на 0.2 секунды
    screen.update()
    time.sleep(0.2)

    # 1. Начинаем цикл, который проходит по всем сегментам змеи, кроме головы (от последнего до второго)
    for seg in range(len(segments) - 1, 0, -1):
        # 2. Получаем координаты сегмента перед текущим сегментом и сохраняем их в переменные new_x и new_y
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        # 3. Перемещаем текущий сегмент на новые координаты (new_x, new_y)
        segments[seg].goto(new_x, new_y)

    # двигаем голову змеи вперед на 20 пикселей
    segments[0].forward(20)

# закрываем экран при клике мыши
screen.exitonclick()