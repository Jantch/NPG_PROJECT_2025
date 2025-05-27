import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("images/game_background.jpg")
background = pygame.transform.scale(background, (800, 600))

# Title and Icon
pygame.display.set_caption('Escape room')
icon = pygame.image.load('images/key.png')
pygame.display.set_icon(icon)

# Game Loop
runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB
    screen.blit(background, (0, 0))
    pygame.display.update()