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
            pygame.draw.rect(screen, (139, 71, 38), (100, 100, 250, s * 80))

            row_height = 70  # dostosuj do wysokości ikon
            icon_size = 128  # bo Twoje ikony są 128x128

            for i, item in enumerate(self.items):
                y = 80 + i * row_height
                icon_x = 60

                # Rysowanie ikony
                item.draw_icon(screen, icon_x, y)

                # Render tekstu
                text = self.font.render(item.name, True, (255, 255, 255))

                # Tworzymy prostokąt ikony (używamy pozycji i znanego rozmiaru)
                icon_rect = pygame.Rect(icon_x, y, icon_size, icon_size)

                # Wyrównanie tekstu względem ikony (pionowo na środku, obok ikony)
                text_rect = text.get_rect()
                text_rect.midleft = (icon_rect.right -40, icon_rect.centery)

                screen.blit(text, text_rect)