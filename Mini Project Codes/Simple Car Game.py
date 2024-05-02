import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Game")

# Colors
LIGHT_PINK = (255, 204, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Set up the clock
clock = pygame.time.Clock()

# Car variables
car_width = 60
car_height = 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10
car_speed = 12

# Obstacle variables
obstacles = []
obstacle_frequency = 60  # Adjust frequency
obstacle_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Functions
def draw_car(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, car_width, car_height))

def draw_obstacle(x, y, width, height):
    pygame.draw.rect(screen, BLACK, (x, y, width, height))

def display_score(score):
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

def display_instructions():
    instruction_text = font.render("Use LEFT and RIGHT arrow keys to move", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, 10))

def display_crash_message():
    crash_text = font.render("You Crashed!", True, BLACK)
    screen.blit(crash_text, (WIDTH // 2 - crash_text.get_width() // 2, HEIGHT // 2 - crash_text.get_height() // 2))

def collision_detection(car_x, car_y, obstacle_x, obstacle_y, obstacle_width, obstacle_height):
    if (car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and
            car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y):
        return True
    return False

# Game loop
running = True
while running:
    screen.fill(LIGHT_PINK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Generate obstacles
    if random.randrange(obstacle_frequency) == 0:
        obstacle_width = random.randint(50, 150)
        obstacle_height = random.randint(20, 50)
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacles.append([obstacle_x, -obstacle_height, obstacle_width, obstacle_height])

    # Update obstacle positions
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)
            score += 1

    # Collision detection
    for obstacle in obstacles:
        if collision_detection(car_x, car_y, obstacle[0], obstacle[1], obstacle[2], obstacle[3]):
            running = False

    # Draw car and obstacles
    draw_car(car_x, car_y)
    for obstacle in obstacles:
        draw_obstacle(obstacle[0], obstacle[1], obstacle[2], obstacle[3])

    # Display score
    display_score(score)
    display_instructions()

    # Display crash message if collision occurs
    for obstacle in obstacles:
        if collision_detection(car_x, car_y, obstacle[0], obstacle[1], obstacle[2], obstacle[3]):
            display_crash_message()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
