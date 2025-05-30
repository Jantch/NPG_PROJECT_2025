import sys
from inicjalization_of_assets import *
from animation_of_transition import transition_animation

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escaperooms")

# Ustawienie tła
background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Ustawienie tła do przejścia
background_2 = pygame.transform.smoothscale(background_2, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Ustawienie tła do natępnego pokoju
background_next_1 = pygame.transform.smoothscale(background_next_1, (SCREEN_WIDTH, SCREEN_HEIGHT))

if_button_display = True
if_other_button_display = True

# Ustawienie przycisku play
play_button = play_button_img_1.get_rect(topleft=(110, 190))

# Ustawienie przycisku exit
exit_button = exit_button_img_1.get_rect(topleft=(110, 300))


# Ustawienie przycisku od dzwięku
sound_button = sound_button_img_1.get_rect(topleft=(25, 700))
current_sound_button_im = sound_button_img_1

# Główna pętla gry
running = True
while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if play_button.collidepoint(event.pos):
                background = background_2
                transition_animation(screen, background, background_next_1)
                background = background_next_1
                if_button_display = False

            if exit_button.collidepoint(event.pos):
                running = False

            if sound_button.collidepoint(event.pos):
                if current_sound_button_im == sound_button_img_1:
                    current_sound_button_im = sound_button_img_2
                else:
                    current_sound_button_im = sound_button_img_1

    # Rysowanie tła
    screen.blit(background, (0, 0))

    if if_button_display:

        # Rysowanie przycisku play
        if play_button.collidepoint(mouse_pos):
            screen.blit(background_2, (0, 0))
            if_other_button_display = False
            screen.blit(play_button_img_2, play_button.topleft)
        else:
            if_other_button_display = True
            screen.blit(play_button_img_1, play_button.topleft)

        # Rsowanie pozostałych przycisków w grze
        if if_other_button_display:

            # Rysowanie przycisku play
            if exit_button.collidepoint(mouse_pos):
                screen.blit(exit_button_img_2, exit_button.topleft)
            else:
                screen.blit(exit_button_img_1, exit_button.topleft)


            # Rysowanie przycisku sound
            screen.blit(current_sound_button_im, sound_button.topleft)

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie
pygame.quit()
sys.exit()
