from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

# создаем экран
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snack game')
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
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
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.win()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.xcor()<-290:
        game_is_on=False
        scoreboard.game_over()



# закрываем экран при клике мыши
screen.exitonclick()