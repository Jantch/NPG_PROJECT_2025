import sys
import os
from inicjalization_of_assets import *
from animation_of_transition import transition_animation

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rooms.room_1 import room_1

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 764
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escaperooms")

# Ustawienie tła
background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_2 = pygame.transform.smoothscale(background_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_next_1 = pygame.transform.smoothscale(background_next_1, (SCREEN_WIDTH, SCREEN_HEIGHT))

if_button_display = True
if_other_button_display = True

# Przyciski
play_button = play_button_img_1.get_rect(topleft=(115, 510))
exit_button = exit_button_img_1.get_rect(topleft=(25, 25))
sound_button = sound_button_img_1.get_rect(topleft=(440, 25))
current_sound_button_im = sound_button_img_1

# Ustawienie soundtracku do menu (room_1.wav)
menu_sound_track_path = os.path.join(SOUND_DIR_soundtrack, "room_1.wav")
menu_sound_track = pygame.mixer.Sound(menu_sound_track_path)
menu_sound_track.play(loops=-1)  # Pętla nieskończona
menu_sound_track.set_volume(1.0)  # Głośność 100%
if_sound_track_active = True

# Dźwięk otwarcia drzwi
door_sound_path = os.path.join(SOUND_DIR_elements, "open_door.wav")
open_door_sound = pygame.mixer.Sound(door_sound_path)
if_sound_open_door_active = False

# Główna pętla gry
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                menu_sound_track.stop()
                background = background_2
                # background = background_next_1
                if_button_display = False
                transition_animation(screen, background, background_next_1)

                # Wejście do pokoju 1
                room_1(screen)
                running = False

            if exit_button.collidepoint(event.pos):
                running = False

            if sound_button.collidepoint(event.pos):
                if if_sound_track_active:
                    menu_sound_track.set_volume(0.0)
                    current_sound_button_im = sound_button_img_2
                    if_sound_track_active = False
                else:
                    menu_sound_track.set_volume(1.0)
                    current_sound_button_im = sound_button_img_1
                    if_sound_track_active = True

    # Rysowanie tła
    screen.blit(background, (0, 0))

    if if_button_display:
        # Rysowanie przycisku play
        if play_button.collidepoint(mouse_pos):
            if not if_sound_open_door_active:
                open_door_sound.play()
                if_sound_open_door_active = True
            screen.blit(background_2, (0, 0))
            if_other_button_display = False
            screen.blit(play_button_img_2, play_button.topleft)
        else:
            if_sound_open_door_active = False
            if_other_button_display = True
            screen.blit(play_button_img_1, play_button.topleft)

        # Pozostałe przyciski
        if if_other_button_display:
            if exit_button.collidepoint(mouse_pos):
                screen.blit(exit_button_img_2, exit_button.topleft)
            else:
                screen.blit(exit_button_img_1, exit_button.topleft)

            screen.blit(current_sound_button_im, sound_button.topleft)

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie
pygame.quit()
sys.exit()

