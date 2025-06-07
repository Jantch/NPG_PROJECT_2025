import pygame


class Item:
    def __init__(self, name: str, icon_path):
        self.name = name
        self.icon = pygame.image.load(icon_path).convert_alpha()
        self.icon = pygame.transform.scale(self.icon, (128, 128))  # ustaw rozmiar ikony

    def draw_icon(self, screen, x, y):
        screen.blit(self.icon, (x, y))