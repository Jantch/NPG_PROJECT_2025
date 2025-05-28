import pygame
from pygame import font


class Inventory:
    def __init__(self):
        self.items = []
        self.open = False


    def toggle(self):
        self.open = not self.open

    def add_item(self, item):
        self.items.append(item)

    def draw(self, screen):
        if self.open:
            # narysuj tło ekwipunku
            pygame.draw.rect(screen, (50, 50, 50), (100, 100, 300, 200))
            # wypisz przedmioty
            for i, item in enumerate(self.items):
                text = font.render(item, True, (255, 255, 255))
                screen.blit(text, (110, 110 + i * 30))