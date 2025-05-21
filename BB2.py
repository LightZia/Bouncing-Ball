import pygame
import pygame_gui
from pygame.locals import QUIT

# Initialize pygame and pygame_gui
pygame.init()
pygame.display.set_caption("Interactive Bouncing Ball Simulation")
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
manager = pygame_gui.UIManager(window_size)

# Constants
FPS = 60

# Initialize sliders and labels
gravity_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((10, 10, 200, 30)),
    start_value=9.8,
    value_range=(0.0, 20.0),
    manager=manager
)
gravity_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 50, 200, 30)),
    text='Gravity: 9.8',
    manager=manager
)

restitution_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((10, 100, 200, 30)),
    start_value=0.8,
    value_range=(0.0, 1.0),
    manager=manager
)
restitution_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 140, 200, 30)),
    text='Restitution: 0.8',
    manager=manager
)

radius_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((10, 190, 200, 30)),
    start_value=20,
    value_range=(5, 50),
    manager=manager
)
radius_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 230, 200, 30)),
    text='Radius: 20',
    manager=manager
)

# Ball properties
x = window_size[0] // 2
y = window_size[1] // 2
dx = 0
dy = 0
ball_color = (255, 0, 0)

clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        manager.process_events(event)

    manager.update(time_delta)

    # Get slider values
    gravity = gravity_slider.get_current_value()
    restitution = restitution_slider.get_current_value()
    radius = radius_slider.get_current_value()

    # Physics updates
    dy += gravity * time_delta  # Apply gravity
    x += dx * time_delta
    y += dy * time_delta

    # Bounce off the bottom
    if y + radius > window_size[1]:
        y = window_size[1] - radius
        dy = -dy * restitution

    # Bounce off the top
    if y - radius < 0:
        y = radius
        dy = -dy * restitution

    # Bounce off the sides
    if x + radius > window_size[0]:
        x = window_size[0] - radius
        dx = -dx * restitution
    if x - radius < 0:
        x = radius
        dx = -dx * restitution

    # Drawing
    screen.fill((0, 0, 0))  # White background
    pygame.draw.circle(screen, ball_color, (int(x), int(y)), int(radius))
    manager.draw_ui(screen)

    pygame.display.flip()
