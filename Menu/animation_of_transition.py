from inicjalization_of_assets import *


def transition_animation(screen, old_surface, new_background, duration=1000):
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # Początkowe parametry
    angle = 0
    scale = 1.0
    max_time = duration  # czas animacji w ms
    old_rect = old_surface.get_rect(center=screen.get_rect().center)

    while True:
        elapsed = pygame.time.get_ticks() - start_time
        if elapsed > max_time:
            break

        # Procent postępu animacji (0 do 1)
        t = elapsed / max_time
        angle = t * 360           # obróć o 360 stopni
        scale = max(0.01, 1 - t)  # zmniejsz do prawie 0

        # Nowe tło już jest
        screen.blit(new_background, (0, 0))

        # Skaluj i obracaj
        scaled_surface = pygame.transform.rotozoom(old_surface, angle, scale)
        new_rect = scaled_surface.get_rect(center=screen.get_rect().center)

        # Wyświetl stary obraz w animacji
        screen.blit(scaled_surface, new_rect.topleft)

        pygame.display.flip()
        clock.tick(60)