import pygame


def add_tile_to_pygame(screen, colour, position, size):
    colour = pygame.Color(colour)
    tile = pygame.draw.rect(screen, colour, pygame.Rect(position[0], position[1], size, size))
    return tile