from game_logic.pygame_instance import PygameInstance
import pygame

game = PygameInstance(800, 600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit()
            exit()

    game.clear_screen()
    game.update_display()