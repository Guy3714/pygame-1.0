import pygame

pygame.init()

white=(255,255,255)
font=pygame.font.SysFont(None,48)

running=True

Counter=0

Width, Height =600, 600
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Click Counter")

screen.fill(white)
pygame.display.flip()

while running:


    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                Counter += 1
            elif event.button == 3:  # Right click
                Counter -= 1
    
    text = font.render(f"{Counter}",True,(0,0,0))
    screen.blit(text, (Width // 2 - text.get_width() // 2, Height // 2 - text.get_height() // 2))   
        
    pygame.display.flip()
pygame.quit()


"""
| Mouse Button         | `event.button` Value |
| -------------------- | -------------------- |
| Left Click           | `1`                  |
| Middle Click (Wheel) | `2`                  |
| Right Click          | `3`                  |
| Scroll Up            | `4`                  |
| Scroll Down          | `5`                  |
"""
