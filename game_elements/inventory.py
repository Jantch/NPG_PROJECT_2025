import pygame



class Inventory:
    def __init__(self):
        self.items = []
        self.open = False
        self.font = pygame.font.SysFont(None, 24)
        self.amount = 0

    def toggle(self):
        self.open = not self.open

    def add_item(self, item):
        self.items.append(item)
        self.amount += 1
        print(f"Dodano do ekwipunku: {item.name}")

    def if_in_inventory(self, item):
        return item in self.items

    def draw(self, screen):
        s = self.amount
        if self.open:
            pygame.draw.rect(screen, (50, 50, 50), (100, 100, 250, s*100))

            row_height = 70  # zwiększamy odstęp między wierszami
            icon_size = 64  # załóżmy, że ikony mają 32x32 px
            text_offset_y = (row_height - 24) // 3  # centrowanie tekstu (24 to rozmiar fonta)

            for i, item in enumerate(self.items):
                y = 110 + i * row_height
                item.draw_icon(screen, 110, y)
                text = self.font.render(item.name, True, (255, 255, 255))
                screen.blit(text, (150, y + text_offset_y))