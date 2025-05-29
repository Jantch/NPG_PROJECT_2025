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

# Ustawienie tła do natępnego pokoju
background_next_1 = pygame.transform.smoothscale(background_next_1, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Ustawienie przycisku play
play_button = play_button_img_1.get_rect(topleft=(110, 190))
if_button_display = True

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
                print("Kliknięto przycisk!")
                transition_animation(screen, background, background_next_1)
                background = background_next_1
                if_button_display = False
                # running = False
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
            screen.blit(play_button_img_2, play_button.topleft)
        else:
            screen.blit(play_button_img_1, play_button.topleft)

        # Rysowanie przycisku sound
        screen.blit(current_sound_button_im, sound_button.topleft)

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie
pygame.quit()
sys.exit()
