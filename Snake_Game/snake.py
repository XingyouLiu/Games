from turtle import Turtle

MOVE_DISTANCE = 20
NUM_OF_SNAKE_UNITS = 3
SIZE_OF_SNAKE_UNIT = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake=self.create_segments()
        self.head=self.snake[0]

    def create_segments(self):
        segments=[]
        for i in range(NUM_OF_SNAKE_UNITS):
            snake_unit = Turtle()
            snake_unit.shape('square')
            snake_unit.color('white')
            snake_unit.penup()
            snake_unit.goto(-SIZE_OF_SNAKE_UNIT * i, 0)
            segments.append(snake_unit)
        return segments

    def extend(self):
        new_snake_unit = Turtle()
        new_snake_unit.shape('square')
        new_snake_unit.color('white')
        new_snake_unit.penup()
        new_snake_unit.goto(self.snake[-1].position())
        self.snake.append(new_snake_unit)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def reset(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.snake = self.create_segments()
        self.head = self.snake[0]