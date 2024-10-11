from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
food.refresh()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(fun=snake.move_up,key="Up")
screen.onkey(fun=snake.move_down,key="Down")
screen.onkey(fun=snake.move_left,key="Left")
screen.onkey(fun=snake.move_right,key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.get_score()
        food.refresh()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        #game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    #if head collides with any segments in the tail: trigger game over
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()