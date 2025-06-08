### room_1.py (zmodyfikowany)

def room_1(screen):
    import pygame
    import sys
    import os
    import subprocess

    from game_elements.card import Card
    from game_elements.inventory import Inventory
    from game_elements.item import Item
    from game_elements.mystery import Mystery
    from openaimodule.aimodule import Hint

    pygame.font.init()

    WIDTH, HEIGHT = screen.get_size()

    # Kolory
    DARK_GRAY = (20, 20, 20)
    HIGHLIGHT = (100, 100, 255)

    BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    BASE_PATH_SOUNDS = os.path.join(BASE_PATH, "sounds", "effects")
    ASSISTANT_PATH_SOUNDS = os.path.join(BASE_PATH, "openaimodule", "hints_voc")

    background = pygame.image.load(os.path.join(BASE_PATH, "assets", "background_v2.jpg"))
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

    equipment_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "backpack.png")).convert_alpha()
    equipment_icon_image = pygame.transform.smoothscale(equipment_image, (100, 100))
    equipment = equipment_icon_image.get_rect(topleft=(10, 10))

    backpack_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "backpack_open.wav"))
    key_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "key_get.wav"))
    soundtrack = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "..", "soundtrack", "room_1.wav"))
    interaction_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "interaction.wav"))

    tictactoe_hitbox = pygame.Rect(90, 600, 150, 150)
    colors_hitbox = pygame.Rect(355, 520, 140, 90)
    hint_hitbox = pygame.Rect(380, 10, 100, 100)
    code_cards_hitbox = pygame.Rect(69, 282, 77, 34)

    key_1_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "key.jpg")).convert_alpha()
    key_1_image.set_alpha(250)
    key_1_icon_image = pygame.transform.scale(key_1_image, (100, 100))
    key_1 = key_1_icon_image.get_rect(midbottom=(WIDTH // 3.2, HEIGHT - 7))

    open_safe_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "otwarty_sejf_sam.jpg")).convert_alpha()
    open_safe_icon_image = pygame.transform.scale(open_safe_image, (318, 210))
    open_safe = open_safe_icon_image.get_rect(midbottom=(WIDTH // 2.57, HEIGHT - -1.2))

    open_locker_image = pygame.image.load(os.path.join(BASE_PATH, "assets", "otwarta_szafka_sama.jpg")).convert_alpha()
    open_locker_icon_image = pygame.transform.scale(open_locker_image, (136, 174))
    open_locker = open_locker_icon_image.get_rect(bottomright=(WIDTH, HEIGHT - 221.5))

    def open_tictactoe():
        return subprocess.run(['python', os.path.join(BASE_PATH, 'minigames', 'tictactoe', 'game.py')])

    def open_colors_game():
        return subprocess.run(['python', os.path.join(BASE_PATH, 'minigames', 'colors', 'game.py')])

    def open_code_cards_game():
        return subprocess.run(['python', os.path.join(BASE_PATH, 'minigames', 'code_cards', 'game.py')])

    soundtrack.set_volume(0.2)
    soundtrack.play(loops=-1)

    tictactoe_mystery = Mystery('tictactoe')
    colors_game_mystery = Mystery('colors_game')
    code_cards_game_mystery = Mystery('code_cards_game')

    dwojka_pik = Item("dwójka pik", os.path.join(BASE_PATH, "assets", "dwojka_pik.png"))
    as_kier = Item("as kier", os.path.join(BASE_PATH, "assets", "as_kier.png"))
    trojka_karo = Item("trójka karo", os.path.join(BASE_PATH, "assets", "trojka_karo.png"))
    siodemka_trefl = Item("siódemka trefl", os.path.join(BASE_PATH, "assets", "siodemka_trefl.png"))

    key_1_item = Item("Klucz", os.path.join(BASE_PATH, "assets", "key.jpg"))
    clock = pygame.time.Clock()
    inv = Inventory()
    inv.add_item(siodemka_trefl)
    completed = []
    #colors_game_mystery.set_as_completed()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if equipment.collidepoint(event.pos):
                    inv.toggle()
                    backpack_sound.play()
                elif tictactoe_hitbox.collidepoint(event.pos) and not tictactoe_mystery.get_status():
                    interaction_sound.play()
                    if open_tictactoe().returncode == 1:
                        tictactoe_mystery.set_as_completed()
                elif key_1.collidepoint(event.pos) and tictactoe_mystery.get_status() and not inv.if_in_inventory(key_1_item):
                    inv.add_item(key_1_item)
                    key_sound.play()
                elif colors_hitbox.collidepoint(event.pos) and not colors_game_mystery.get_status():
                    interaction_sound.play()
                    if open_colors_game().returncode == 1:
                        colors_game_mystery.set_as_completed()
                elif hint_hitbox.collidepoint(event.pos):
                    hint = Hint()
                    hint.get_hint(completed)
                    assistant_sound = pygame.mixer.Sound(os.path.join(ASSISTANT_PATH_SOUNDS, "sound_of_assistant.wav"))
                    assistant_sound.play()
                elif code_cards_hitbox.collidepoint(event.pos) and not inv.if_in_inventory(siodemka_trefl):
                    if open_code_cards_game().returncode == 1:
                        inv.add_item(siodemka_trefl)
                        code_cards_game_mystery.set_as_completed()

        screen.blit(background, (0, 0))
        screen.blit(equipment_icon_image, equipment)
        pygame.draw.rect(screen, (255, 0, 0), hint_hitbox)

        if tictactoe_mystery.get_status():
            screen.blit(open_safe_icon_image, open_safe)
            completed.append("kółko i krzyżyk")

        if colors_game_mystery.get_status():
            screen.blit(open_locker_icon_image, open_locker)
            completed.append("układanie klocków")

        if inv.open:
            inv.draw(screen)

        pygame.display.flip()
        clock.tick(60)