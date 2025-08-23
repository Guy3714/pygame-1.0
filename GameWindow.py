import pygame

pygame.init()

BLUE = (0, 0, 255)

running = True

Width, Height = 500, 200
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Window")


while running:
    screen.fill(BLUE)

    pygame.display.flip()




    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running=false