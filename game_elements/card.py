import pygame

#rank - numerek albo np król
#suit - kolor w sensie pik trefl karo i kier
# pik to takie czarne odwrócone serduszko
# trefl to taka czarna koniczynka
# karo to czerwony romb
# kier to czerwone serce
#tłumaczenie specjalnie dla ciebei Erysk Szalka <3 :*

class Card:
    def __init__(self, rank: str, suit: str, icon_path):
        self.rank = rank
        self.suit = suit
        self.icon = pygame.image.load(icon_path).convert_alpha()
        self.icon = pygame.transform.scale(self.icon, (32, 32)) #rozmiar ikony karty - trzeba to bedzie zmienić

    def draw_icon(self, screen, x, y):
        screen.blit(self.icon, (x, y))