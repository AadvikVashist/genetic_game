import pygame

# Initialize pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color to white
background_color = (255, 255, 255)

# Fill the screen with the background color
screen.fill(background_color)
# Update the screen
pygame.display.flip()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
