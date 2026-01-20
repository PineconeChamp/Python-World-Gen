import pygame


def add_tile_to_pygame(game, position, size):
    tile = pygame.draw.rect(game, "blue", pygame.Rect(position[0], position[1], size, size))
    return tile