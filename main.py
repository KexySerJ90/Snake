from turtle import Screen
from snake import Snake
import time

# создаем экран
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snack game')
screen.tracer(0)

snake=Snake()
# Ожидание нажатия клавиш на экране
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')



# запускаем игру
game_is_on = True
while game_is_on:
    # обновляем экран и задерживаем выполнение на 0.2 секунды
    screen.update()
    time.sleep(0.2)

    snake.move()



# закрываем экран при клике мыши
screen.exitonclick()