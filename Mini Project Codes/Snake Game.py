import turtle
import time
import random

delay = 0.07  # Adjusted for smoother animation
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("pink")
wn.setup(width=700, height=700)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shapesize(1, 1)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0, 100)

segments = []

# Adding text for controls
control_text = turtle.Turtle()
control_text.speed(0)
control_text.color("white")
control_text.penup()
control_text.hideturtle()
control_text.goto(0, -280)
control_text.write("Use WASD or Arrow keys to move", align="center", font=("Cambria", 20, "bold"))


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0     High Score: 0", align="center", font=("Cambria", 25, "bold"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "Right")

# Function to reset the game
def reset_game():
    global score
    global high_score
    global segments

    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()

    # Reset the score
    score = 0
    pen.clear()
    pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Cambria", 25, "bold"))

# Main game loop
while True:
    wn.update()

    # Check for collision with the border
    if head.xcor() > 700 or head.xcor() < -700 or head.ycor() > 700 or head.ycor() < -700:
        reset_game()

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Increase the score
        score += 100

        # Update the high score if necessary
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Cambria", 25, "bold"))

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with body segments (except the first segment)
    for segment in segments[1:]:
        if head.distance(segment) < 20:
            reset_game()

    time.sleep(delay)
