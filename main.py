import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.change_position()
        snake.extend_snake()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 240:
        scoreboard.reset()
        snake.reset()

    elif snake.head.xcor() < -240:
        scoreboard.reset()
        snake.reset()

    elif snake.head.ycor() > 240:
        scoreboard.reset()
        snake.reset()

    elif snake.head.ycor() < -240:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
