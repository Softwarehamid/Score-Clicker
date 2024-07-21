import pygame

import random

pygame.init()

running = True

screen = pygame.display.set_mode((1280,720))

pos = pygame.Vector2(200,200)


clock = pygame.time.Clock()

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Do logical updates here.
    # ...

    screen.fill("white")  # Fill the display with a solid color 

    pygame.draw.circle(screen, "Purple", pos, 40)

    

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(120)         # wait until next frame (at 60 FPS)

pygame.quit()