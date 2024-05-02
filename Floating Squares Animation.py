import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=900, height=500)
screen.bgcolor("#8800ff")  # Hexadecimal color for light purple
screen.tracer(0)

# Define a function to create a square
def create_square(color):
    square = turtle.Turtle()
    square.shape("square")
    square.color(color)
    square.penup()
    square.speed(0)
    return square

# Create 77 squares
squares = []
colors = ["#9500ba", "#ffffff", "#00fbff", "#26ff00", "#ffff00", "#000000", "#ff0000"]
for _ in range(77):
    color = random.choice(colors)
    square = create_square(color)
    square.goto(random.randint(-380, 380), random.randint(-280, 280))  # Random initial position
    square.dx = random.uniform(-2, 2)  # Random horizontal speed
    square.dy = random.uniform(-2, 2)  # Random vertical speed
    squares.append(square)

# Define a function to move the squares
def move_squares():
    for square in squares:
        square.setx(square.xcor() + square.dx)
        square.sety(square.ycor() + square.dy)

        # Border checking
        if square.xcor() > 390 or square.xcor() < -390:
            square.dx *= -1
        if square.ycor() > 290 or square.ycor() < -290:
            square.dy *= -1

# Main animation loop
while True:
    screen.update()
    move_squares()




