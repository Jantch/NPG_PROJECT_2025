import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Escape room')
icon = pygame.image.load('key.png')
pygame.display.set_icon(icon)

# Game Loop
runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB
    screen.fill((0,0,255))
    pygame.display.update()