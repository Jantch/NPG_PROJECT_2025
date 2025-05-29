import pygame



class Inventory:
    def __init__(self):
        self.items = []
        self.open = False
        self.font = pygame.font.SysFont(None, 24)

    def toggle(self):
        self.open = not self.open

    def add_item(self, item):
        self.items.append(item)

    def if_in_inventory(self, item):
        return item in self.items

    def draw(self, screen):
        if self.open:
            # narysuj tło ekwipunku
            pygame.draw.rect(screen, (50, 50, 50), (100, 100, 300, 200))
            # wypisz przedmioty
            for i, item in enumerate(self.items):
                item.draw_icon(screen, 110, 110 + i * 40)
                text = self.font.render(item.name, True, (255, 255, 255))
                screen.blit(text, (150, 110 + i * 40 + 8))