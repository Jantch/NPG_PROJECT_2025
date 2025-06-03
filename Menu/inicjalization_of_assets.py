import os
import pygame

# Ustawienie bazowej ścieżki na folder, w którym znajduje się ten plik .py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ścieżka do folderu z obrazami
IMG_DIR = os.path.join(BASE_DIR, "..", "assets", "images_in_menu")

# Ścieżka do folderu z dźwiękami
SOUND_DIR = os.path.join(BASE_DIR, "..", "sounds", "effects")

# Tło
image_path_background = os.path.join(IMG_DIR, "background.png")
background = pygame.image.load(image_path_background)

image_path_background_2 = os.path.join(IMG_DIR, "background_2.png")
background_2 = pygame.image.load(image_path_background_2)

image_path_background_next_1 = os.path.join(IMG_DIR, "temporary_background.jpg")
background_next_1 = pygame.image.load(image_path_background_next_1)

# Przycisk PLAY
image_path_play_button_1 = os.path.join(IMG_DIR, "Play_Button_1.png")
play_button_img_1 = pygame.image.load(image_path_play_button_1)
play_button_img_1 = pygame.transform.scale(play_button_img_1, (300, 100))

image_path_play_button_2 = os.path.join(IMG_DIR, "Play_Button_2.png")
play_button_img_2 = pygame.image.load(image_path_play_button_2)
play_button_img_2 = pygame.transform.scale(play_button_img_2, (300, 100))

# Przycisk EXIT
image_path_exit_button_1 = os.path.join(IMG_DIR, "back_button_1.png")
exit_button_img_1 = pygame.image.load(image_path_exit_button_1)
exit_button_img_1 = pygame.transform.scale(exit_button_img_1, (50, 50))

image_path_exit_button_2 = os.path.join(IMG_DIR, "back_button_2.png")
exit_button_img_2 = pygame.image.load(image_path_exit_button_2)
exit_button_img_2 = pygame.transform.scale(exit_button_img_2, (50, 50))

# Przycisk DŹWIĘKU
image_path_sound_1 = os.path.join(IMG_DIR, "Audio_button_1.png")
sound_button_img_1 = pygame.image.load(image_path_sound_1)
sound_button_img_1 = pygame.transform.scale(sound_button_img_1, (50, 50))

image_path_sound_2 = os.path.join(IMG_DIR, "Audio_button_2.png")
sound_button_img_2 = pygame.image.load(image_path_sound_2)
sound_button_img_2 = pygame.transform.scale(sound_button_img_2, (50, 50))



