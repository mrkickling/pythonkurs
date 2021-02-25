# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
# Run until the user asks to quit
running = True

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("LEFT KEY")
            if event.key == pygame.K_RIGHT:
                print("RIGHT KEY")

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (100, 100), 75)
    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
