import os

import pygame

# Ścieżka do tła
image_path_background = os.path.join("..", "assets", "images", "background.png")
background = pygame.image.load(image_path_background)

# Ścieżka do tła przejścia
image_path_background_2 = os.path.join("..", "assets", "images", "background_2.png")
background_2 = pygame.image.load(image_path_background_2)

# Ścieżka do tła w następnym levelu
image_path_background_next_1 = os.path.join("..", "assets", "images", "temporary_background.jpg")
background_next_1 = pygame.image.load(image_path_background_next_1)

# Ustawienie ścieżek do przycisków

# Pierwsze zdjecie do przycisku play
image_path_play_button_1 = os.path.join("..", "assets", "images", "Play_Button_1.png")
play_button_img_1 = pygame.image.load(image_path_play_button_1)
play_button_img_1 = pygame.transform.scale(play_button_img_1, (300, 100))

# Drugie zdjecie do przycisku play
image_path_play_button_2 = os.path.join("..", "assets", "images", "Play_Button_2.png")
play_button_img_2 = pygame.image.load(image_path_play_button_2)
play_button_img_2 = pygame.transform.scale(play_button_img_2, (300, 100))

# Pierwsze zdjecie do przyciku exit
image_path_exit_button_1 = os.path.join("..", "assets", "images", "back_button_1.png")
exit_button_img_1 = pygame.image.load(image_path_exit_button_1)
exit_button_img_1 = pygame.transform.scale(exit_button_img_1, (50, 50))

# Drugie zdjecie do przyciku exit
image_path_exit_button_2 = os.path.join("..", "assets", "images", "back_button_2.png")
exit_button_img_2 = pygame.image.load(image_path_exit_button_2)
exit_button_img_2 = pygame.transform.scale(exit_button_img_2, (50, 50))


# Drugie zdje

# Pierwsze zdjecie do przycisku dzwięku
image_path_sound_1 = os.path.join("..", "assets", "images", "Audio_button_1.png")
sound_button_img_1 = pygame.image.load(image_path_sound_1)
sound_button_img_1 = pygame.transform.scale(sound_button_img_1, (50, 50))

# Drugie zdjecie do przycisku dzwięku
image_path_sound_2 = os.path.join("..", "assets", "images", "Audio_button_2.png")
sound_button_img_2 = pygame.image.load(image_path_sound_2)
sound_button_img_2 = pygame.transform.scale(sound_button_img_2, (50, 50))