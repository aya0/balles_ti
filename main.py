import pygame
import math 

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill background black
    # Draw a arc 
    pygame.draw.arc(screen , (250,250,250) , (300, 200, 200, 200) , 0 , 3*math.pi/2 , 2)
    pygame.display.flip()  # Update screen

pygame.quit()
