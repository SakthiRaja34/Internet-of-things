import pygame
import sys
import random

pygame.init()

# screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

# paddle
paddle_width = 100
paddle_height = 15
paddle_x = WIDTH//2 - paddle_width//2
paddle_y = HEIGHT - 30
paddle_speed = 7

# ball
ball_radius = 15
ball_x = random.randint(0, WIDTH)
ball_y = 0
ball_speed = 4

score = 0
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # move ball
    ball_y += ball_speed

    # collision
    if (paddle_y < ball_y + ball_radius < paddle_y + paddle_height and
        paddle_x < ball_x < paddle_x + paddle_width):
        score += 1
        ball_y = 0
        ball_x = random.randint(0, WIDTH)

    # game over
    if ball_y > HEIGHT:
        print("Game Over! Score:", score)
        running = False

    # draw
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10,10))

    pygame.display.flip()

pygame.quit()
sys.exit()