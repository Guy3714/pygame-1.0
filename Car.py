import pygame
import random
import sys

pygame.init()

width, height = 800, 1000
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Window")


WHITE=(255, 255, 255)
blue=(0,0,255)

score=0
font = pygame.font.SysFont(None, 36)

car_width=50
car_height=100
car_x=width//2 - car_width//2
car_y=height - car_height -20
car_speed=2
player_car=pygame.Rect(car_x,car_y,car_width,car_height)

block_width = 50
block_height = 100
block_speed = 1
blocks = []

SPAWN_BLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BLOCK, 200)

running=True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, blue, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_BLOCK:
            block_x = random.randint(0, width - block_width)
            block_y = -block_height
            blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_car .left > 0:
        player_car.x -= car_speed
    if keys[pygame.K_RIGHT] and player_car.right < width:
        player_car.x += car_speed

    for block in blocks:
        block.y += block_speed
        if block.y > height:
            blocks.remove(block)
            score += 1

        if player_car.colliderect(block):
            running = False
        pygame.draw.rect(screen, (255,0,0), block)

    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.display.quit()
pygame.quit()