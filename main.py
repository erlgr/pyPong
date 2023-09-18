import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 0.6
PADDLE_SPEED = 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Create paddles and ball
paddle_width, paddle_height = 15, 100
ball_width, ball_height = 15, 15
paddle_speed = PADDLE_SPEED

player_paddle = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_height // 2, ball_width, ball_height)

# Ball movement variables
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# Scores
player_score = 0
opponent_score = 0

# Create fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += paddle_speed

    # Update ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x = -ball_speed_x

    if ball.left <= 0:
        opponent_score += 1
        ball = pygame.Rect(WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_height // 2, ball_width, ball_height)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))

    if ball.right >= WIDTH:
        player_score += 1
        ball = pygame.Rect(WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_height // 2, ball_width, ball_height)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))

    # Opponent AI
    if opponent_paddle.top < ball.y:
        opponent_paddle.y += paddle_speed
    if opponent_paddle.bottom > ball.y:
        opponent_paddle.y -= paddle_speed

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (50, 50))
    screen.blit(opponent_text, (WIDTH - 50 - opponent_text.get_width(), 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
