import pygame
import random
pygame.init()

# Initialize variables
Score = 0

font = pygame.font.Font(None,80)

running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Initial position of the circle
pos = pygame.Vector2(random.randrange(100, 1100), random.randrange(100, 700))

# Time variables
spawn_rate = 700 # Spawn rate in milliseconds (1000 ms = 1 second)
last_spawn_time = pygame.time.get_ticks()  # Get the current time in milliseconds

while running:
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
    if current_time - last_spawn_time > spawn_rate:
        pos = pygame.Vector2(random.randrange(100, 1100), random.randrange(100, 700))
        last_spawn_time = current_time  # Update the last spawn time
    # Process player inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONUP:
            poss = pygame.Vector2(event.pos)
            distance = poss.distance_to(pos)

            if distance < 40:
                print("+1")
                Score += 1

    # Check if it's time to spawn a new circle


    # Do logical updates here
    # ...  
    # event listener for click
    ev = pygame.event.get()
    # Fill the display with a solid color
    screen.fill("white")

    ScoreBoard = font.render(f"Score: {Score} ", True,(255, 255, 255), (0, 0, 255))
    screen.blit(ScoreBoard,(100,100))
    # Draw the circle
    pygame.draw.circle(screen, "Purple", pos, 40)

    # Render the graphics here
    # ...

    

    # Refresh on-screen display
    pygame.display.flip()
    clock.tick(60)  # Wait until next frame (at 60 FPS)

pygame.quit()