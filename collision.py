import pygame

pygame.init()

White = (255,255,255)
blue = (0,0,255)

running = True

Width, Height = 600, 600
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Window")

x=Width//2
y=Height//2
radius= 30
speed= 2

while running:
    screen.fill(White)
    pygame.draw.circle(screen,blue,(x,y),radius)

    if x-radius <= 0 or x+radius >= Width or y-radius <= 0 or y+radius >= Height:
        running  = False

    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

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


