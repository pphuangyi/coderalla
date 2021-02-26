#! /usr/bin/python3

import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    # Did the user click the window close button?    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background with white
    screen.fill((200, 200, 255))
    
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    # Updates the contens of the display to the screen.
    # Without this call, nothing appears in the window.
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
