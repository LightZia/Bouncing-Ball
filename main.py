import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up fullscreen display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Bouncing Circle with Gravity")

# Get screen dimensions
screen_width, screen_height = screen.get_size()

# Calculate the center of the screen
center_x = screen_width // 2

# Gravity and physics variables
gravity = 9.8  # Constant acceleration
velocity = 0  # Initial velocity
e = 0.8  # Energy loss on bounce (less than 1 for realism)

# Circle properties
circle_y = 0  # Start at the top of the screen
circle_radius = 30
circle_color = (255, 0, 0)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity
    velocity += gravity
    circle_y += velocity

    # Bounce when hitting the bottom
    if circle_y + circle_radius > screen_height:
        circle_y = screen_height - circle_radius
        velocity = -velocity * e

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (center_x, int(circle_y)), circle_radius)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
