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
    # обновляем экран
    screen.update()
    if len(snake.segments)>8:
        time.sleep(0.1)
    else:
        time.sleep(0.2)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.win()
    #Если змея выходит за границы поля или сталкивается с каким-то из своих сегментов, то завершить игру и вывести сообщение о конце игры.
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.xcor()<-290:
        scoreboard.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            scoreboard.reset()
            snake.reset()


# закрываем экран при клике мыши
screen.exitonclick()