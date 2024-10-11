import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle=Paddle(-350,0)
r_paddle=Paddle(350,0)

ball=Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

scoreboard.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect if ball is missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


screen.exitonclick()