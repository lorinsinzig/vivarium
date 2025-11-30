import pygame

# Initiate game
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Main loop
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, 'red', player_pos, 20) # What screen, color, screen-coordinates, width

    pygame.display.update() # Update the screen every frame
    clock.tick(60) # Limit to 60FPS