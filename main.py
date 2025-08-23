import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Square")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Square setup
square_size = 50
square_x = random.randint(0, WIDTH - square_size)
square_y = random.randint(0, HEIGHT - square_size)

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw square
    square = pygame.Rect(square_x, square_y, square_size, square_size)
    pygame.draw.rect(screen, BLUE, square)

    # Draw score
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if square.collidepoint(event.pos):
                score += 1
                square_x = random.randint(0, WIDTH - square_size)
                square_y = random.randint(0, HEIGHT - square_size)

    pygame.display.flip()

# Quit
pygame.quit()
