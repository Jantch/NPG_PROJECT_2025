from inicjalization_of_assets import *


def transition_animation(screen, old_surface, new_background, duration=1000):
    clock = pygame.time.Clock()
    center = screen.get_rect().center

    # Parametry
    max_time = duration
    zoom_start = 1.0
    zoom_peak = 3.5

    # --- FAZA 1: Zoom-in starego ekranu + rozjaśnianie ---
    start_time = pygame.time.get_ticks()
    while True:
        elapsed = pygame.time.get_ticks() - start_time
        if elapsed > max_time:
            break

        t = elapsed / max_time
        scale = zoom_start + t * (zoom_peak - zoom_start)  # 1.0 -> 3.5
        zoomed_old = pygame.transform.rotozoom(old_surface, 0, scale)
        zoomed_rect = zoomed_old.get_rect(center=center)

        screen.blit(new_background, (0, 0))  # nowy pokój już pod spodem
        screen.blit(zoomed_old, zoomed_rect)

        # Rozjaśnianie
        fade_surface = pygame.Surface(screen.get_size())
        fade_surface.fill((255, 255, 255))
        fade_surface.set_alpha(int(t * 255))
        screen.blit(fade_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    # --- FAZA 2: Zoom-out nowego pokoju + ściemnianie ---
    start_time = pygame.time.get_ticks()
    while True:
        elapsed = pygame.time.get_ticks() - start_time
        if elapsed > max_time:
            break

        t = elapsed / max_time
        scale = zoom_peak - t * (zoom_peak - zoom_start)  # 3.5 -> 1.0
        zoomed_new = pygame.transform.rotozoom(new_background, 0, scale)
        zoomed_rect = zoomed_new.get_rect(center=center)

        screen.blit(zoomed_new, zoomed_rect)

        # Ściemnianie (z bieli do 0)
        fade_surface = pygame.Surface(screen.get_size())
        fade_surface.fill((255, 255, 255))
        fade_surface.set_alpha(int((1 - t) * 255))
        screen.blit(fade_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)


