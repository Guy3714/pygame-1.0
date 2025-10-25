import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Dodge Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)   # Player car
RED = (255, 0, 0)    # Obstacles
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player car
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 7
player_car = pygame.Rect(car_x, car_y, car_width, car_height)

# Obstacles
block_width = 50
block_height = 100
block_speed = 5
blocks = []

# Spawn a new block every 1 second
SPAWN_BLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BLOCK, 1000)

# Score
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_BLOCK:
            block_x = random.randint(0, WIDTH - block_width)
            block_rect = pygame.Rect(block_x, -block_height, block_width, block_height)
            blocks.append(block_rect)

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_car.left > 0:
        player_car.x -= car_speed
    if keys[pygame.K_RIGHT] and player_car.right < WIDTH:
        player_car.x += car_speed

    # Move obstacles
    for block in blocks[:]:
        block.y += block_speed
        if block.y > HEIGHT:
            blocks.remove(block)
            score += 1  # Increase score for dodged block

        # Collision detection
        if player_car.colliderect(block):
            running = False  # Game Over

    # Draw player car
    pygame.draw.rect(screen, BLUE, player_car)

    # Draw obstacles
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Game Over screen
screen.fill(WHITE)
game_over_text = font.render("Game Over!", True, RED)
final_score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
