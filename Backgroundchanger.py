import pygame
import random

pygame.init()

white=(255,255,255)

running=True

Width, Height =600, 600
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Window")

screen.fill(white)
pygame.display.flip()

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    key=pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        val1=random.randint(0,255)
        val2=random.randint(0,255)
        val3= random.randint(0,255)

        color=(val1,val2,val3)
        
        screen.fill(color)
        pygame.display.flip()
pygame.quit()