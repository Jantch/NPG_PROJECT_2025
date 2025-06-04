import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game_elements.inventory import Inventory
from game_elements.item import Item
import subprocess
from game_elements.mystery import Mystery
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)
from openaimodule.aimodule import Hint

pygame.init()
pygame.font.init()

# Ustawienia okna
WIDTH, HEIGHT = 512, 764
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tajemnicza Gra")

# Kolory
DARK_GRAY = (20, 20, 20)
HIGHLIGHT = (100, 100, 255)

# Ścieżka bazowa względem pliku room_1.py (czyli jeden poziom wyżej)
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Ścieżka bazowa względem pliku room_1.py dla dźwięków
BASE_PATH_SOUNDS = os.path.abspath(os.path.join(BASE_PATH, "sounds", "effects"))
ASSISTANT_PATH_SOUNDS = os.path.abspath(os.path.join(BASE_PATH, "openaimodule", "hints_voc"))
# Ładowanie grafik
background = pygame.image.load(os.path.join(BASE_PATH, "assets", "background_v2.jpg"))
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

equipment_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "backpack.png")).convert_alpha()
equipment_icon_image = pygame.transform.smoothscale(equipment_image, (100, 100))
equipment = equipment_icon_image.get_rect(topleft=(10, 10))

# Ładowanie dźwięków
backpack_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "backpack_open.wav"))
key_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "key_get.wav"))
soundtrack = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "..", "soundtrack", "room_1.wav"))
interaction_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "interaction.wav"))

# Przycisk do gry w tictactoe
tictactoe_hitbox = pygame.Rect(90, 600, 150, 150)

# Ikona klucza
key_1_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "key.jpg")).convert_alpha()
key_1_image.set_alpha(250)
key_1_icon_image = pygame.transform.scale(key_1_image, (100, 100))
key_1 = key_1_icon_image.get_rect(midbottom=(WIDTH // 3.2, HEIGHT - 7))

# Skala ikon
icon_size = (100, 100)

# Przycisk do gry w kolorki
colors_hitbox = pygame.Rect(355, 520, 140, 90)

# Testowy przycisk do podpowiedzi
hint_hitbox = pygame.Rect(380, 10, 100, 100)

# Otwarty sejf
open_safe_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "otwarty_sejf_sam.jpg")).convert_alpha()
open_safe_image.set_alpha(255)
open_safe_icon_image = pygame.transform.scale(open_safe_image, (318, 210))
open_safe = open_safe_icon_image.get_rect(midbottom=(WIDTH // 2.57, HEIGHT --1.2))

# Otwarta szafka
open_locker_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "otwarta_szafka_sama.jpg")).convert_alpha()
open_locker_image.set_alpha(255)
open_locker_icon_image = pygame.transform.scale(open_locker_image, (136, 174))
open_locker = open_locker_icon_image.get_rect(bottomright=(WIDTH , HEIGHT -221.5 ))

def handle_click():
    mouse_pos = pygame.mouse.get_pos()

def open_tictactoe():
    return subprocess.run(['python', os.path.join(BASE_PATH, 'minigames', 'tictactoe', 'game.py')])

def open_colors_game():
    return subprocess.run(['python', os.path.join(BASE_PATH, 'minigames', 'colors', 'game.py')])

def main():
    soundtrack.set_volume(0.2)  #ambient muzyczny
    soundtrack.play(loops=-1)

    tictactoe_mystery = Mystery('tictactoe')
    colors_game_mystery = Mystery('colors_game')
    key_1_item = Item("Klucz", os.path.join(BASE_PATH, "assets", "key.jpg"))
    clock = pygame.time.Clock()
    inv = Inventory()
    completed = []
    #tictactoe_mystery.set_as_completed() #do ustawiania tych ikon po otwarciu
    #colors_game_mystery.set_as_completed() #do ustawiania tych ikon po otwarciu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if equipment.collidepoint(event.pos):
                    inv.toggle()
                    backpack_sound.play()
                elif tictactoe_hitbox.collidepoint(event.pos) and not tictactoe_mystery.get_status():
                    interaction_sound.play()    #dźwiek
                    if open_tictactoe().returncode == 1:
                        tictactoe_mystery.set_as_completed()
                elif key_1.collidepoint(event.pos) and tictactoe_mystery.get_status() and not inv.if_in_inventory(key_1_item):
                    inv.add_item(key_1_item)
                    key_sound.play()
                elif colors_hitbox.collidepoint(event.pos) and not colors_game_mystery.get_status():
                    interaction_sound.play()  # dźwiek
                    if open_colors_game().returncode == 1:
                        colors_game_mystery.set_as_completed()

                elif hint_hitbox.collidepoint(event.pos):
                    hint = Hint()
                    hint.get_hint(completed)
                    assistant_sound = pygame.mixer.Sound(os.path.join(ASSISTANT_PATH_SOUNDS, "sound_of_assistant.wav"))
                    assistant_sound.play()

        SCREEN.blit(background, (0, 0))
        SCREEN.blit(equipment_icon_image, equipment)
        pygame.draw.rect(SCREEN, (255, 0, 0), hint_hitbox)
        

        if tictactoe_mystery.get_status():
            SCREEN.blit(open_safe_icon_image, open_safe)
            completed.append("kółko i krzyzyk")

        if colors_game_mystery.get_status():
            SCREEN.blit(open_locker_icon_image, open_locker)
            completed.append("układanie klocków")

        if inv.open:
            inv.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
