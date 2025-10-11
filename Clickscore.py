# import pygame
# import random
# import math

# pygame.init()


# white=(255,255,255)
# black=(0,0,0)
# red=(255,0,0)

# running=True

# Width, Height= 600, 600
# screen = pygame.display.set_mode((Width,Height))
# pygame.display.set_caption("Click score")
# font = pygame.font.SysFont(None, 36)

# circle_radius=40
# circle_x=random.randint(circle_radius,Width-circle_radius)
# circle_y=random.randint(circle_radius,Height-circle_radius)
# score=0

# clock = pygame.time.Clock()

# while running:


#     screen.fill(white)

#     pygame.draw.circle(screen,red,(circle_x,circle_y),circle_radius)
#     score_text=font.render(f"{score}",True,black)
#     screen.blit(score_text, (10, 10))

#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False

#         if event.type==pygame.MOUSEBUTTONDOWN:
#             mouse_x,mouse_y=pygame.mouse.get_pos()
#             distance=math.hypot(mouse_x-circle_x,mouse_y-circle_y)

#             if distance<=circle_radius:
#                 score=score+1
#                 circle_x=random.randint(circle_radius,Width-circle_radius)
#                 circle_y=random.randint(circle_radius,Height-circle_radius)

#     pygame.display.flip()
#     clock.tick(10)

#     if 
#         pygame.quit()



# pygame.quit()



"fix clock timer homework"
# /


# ---

# import pygame
# import random
# import math
# import sys

# pygame.init()

# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)

# # Screen setup
# Width, Height = 600, 600
# screen = pygame.display.set_mode((Width, Height))
# pygame.display.set_caption("Click the Circle")
# font = pygame.font.SysFont(None, 36)

# # Circle setup
# circle_radius = 40
# circle_x = random.randint(circle_radius, Width - circle_radius)
# circle_y = random.randint(circle_radius, Height - circle_radius)
# score = 0

# # Timer setup
# total_time = 30  # seconds
# start_ticks = pygame.time.get_ticks()

# # Clock for FPS
# clock = pygame.time.Clock()
# FPS = 60

# running = True
# while running:
#     screen.fill(white)

#         # Calculate time left
#             seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
#                 time_left = max(0, total_time - seconds_passed)

#                     if time_left <= 0:
#                             running = False  # End game when time runs out

#                                 # Draw circle
#                                     pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

#                                         # Display score
#                                             score_text = font.render(f"Score: {score}", True, black)
#                                                 screen.blit(score_text, (10, 10))

#                                                     # Display time
#                                                         time_text = font.render(f"Time: {time_left}s", True, black)
#                                                             screen.blit(time_text, (Width - 150, 10))

#                                                                 # Handle events
#                                                                     for event in pygame.event.get():
#                                                                             if event.type == pygame.QUIT:
#                                                                                         pygame.quit()
#                                                                                                     sys.exit()

#                                                                                                             if event.type == pygame.MOUSEBUTTONDOWN:
#                                                                                                                         mouse_x, mouse_y = pygame.mouse.get_pos()
#                                                                                                                                     distance = math.hypot(mouse_x - circle_x, mouse_y - circle_y)

#                                                                                                                                                 if distance <= circle_radius:
#                                                                                                                                                                 score += 1
#                                                                                                                                                                                 # Move to new random location
#                                                                                                                                                                                                 circle_x = random.randint(circle_radius, Width - circle_radius)
#                                                                                                                                                                                                                 circle_y = random.randint(circle_radius, Height - circle_radius)

#                                                                                                                                                                                                                     pygame.display.flip()
#                                                                                                                                                                                                                         clock
import pygame
import random
import math
import sys

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Screen setup
Width, Height = 600, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Click the Circle")
font = pygame.font.SysFont(None, 36)

# Circle setup
circle_radius = 40
circle_x = random.randint(circle_radius, Width - circle_radius)
circle_y = random.randint(circle_radius, Height - circle_radius)
score = 0

# Timer setup
total_time = 30  # seconds
start_ticks = pygame.time.get_ticks()

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    screen.fill(white)

    # Calculate time left
    seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = max(0, total_time - seconds_passed)

    if time_left <= 0:
        running = False  # End game when time runs out

    # Draw circle
    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

    # Display score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Display time
    time_text = font.render(f"Time: {time_left}s", True, black)
    screen.blit(time_text, (Width - 150, 10))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = math.hypot(mouse_x - circle_x, mouse_y - circle_y)

            if distance <= circle_radius:
                score += 1
                # Move to new random location
                circle_x = random.randint(circle_radius, Width - circle_radius)
                circle_y = random.randint(circle_radius, Height - circle_radius)

    pygame.display.flip()
    clock.tick(FPS)

# Quit immediately when time runs out
pygame.quit()
