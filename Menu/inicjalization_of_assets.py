import os

import pygame

# Ścieżka do tła
image_path_background = os.path.join("..", "assets", "images", "background.png")
background = pygame.image.load(image_path_background)

# Ścieżka do tła w następnym levelu
image_path_background_next_1 = os.path.join("..", "assets", "images", "temporary_background.jpg")
background_next_1 = pygame.image.load(image_path_background_next_1)

# Ustawienie ścieżek do przycisków

# Pierwsze zdjecie do przycisku
image_path_play_button_1 = os.path.join("..", "assets", "images", "Play_Button_1.png")
play_button_img_1 = pygame.image.load(image_path_play_button_1)
play_button_img_1 = pygame.transform.scale(play_button_img_1, (300, 100))

# Drugie zdjecie do przycisku
image_path_play_button_2 = os.path.join("..", "assets", "images", "Play_Button_2.png")
play_button_img_2 = pygame.image.load(image_path_play_button_2)
play_button_img_2 = pygame.transform.scale(play_button_img_2, (300, 100))

