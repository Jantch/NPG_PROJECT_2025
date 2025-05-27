import pygame
import sys

pygame.init()

# Ustawienia okna
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tajemnicza Gra")

# Kolory
DARK_GRAY = (20, 20, 20)
HIGHLIGHT = (100, 100, 255)

# Ładowanie grafik
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))



# Skala ikon
icon_size = (100, 100)

@app.route('/strona2')
def strona2():
    return render_template('graj.html')

# Pozycje ikon




def handle_click():
    mouse_pos = pygame.mouse.get_pos()


def main():
    clock = pygame.time.Clock()
    while True:
        SCREEN.fill(DARK_GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click()
        clock.tick(60)

if __name__ == "__main__":
    main()