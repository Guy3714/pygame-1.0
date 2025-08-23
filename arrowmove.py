import pygame

pygame.init()

White = (255,255,255)
blue = (0,0,255)

running = True

Width, Height = 2000, 2000
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Window")

x=Width//2
y=Height//2
radius= 30
speed= 22

while running:
    screen.fill(White)
    pygame.draw.circle(screen,blue,(x,y),radius)
    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=false

    key=pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        x=x-speed
    if key[pygame.K_RIGHT]:
        x=x+speed
    if key[pygame.K_UP]:
        y=y-speed
    if key[pygame.K_DOWN]:
        y=y+speed
    pygame.display.flip()
pygame.quit()