from game_logic.pygame_instance import PygameInstance
from game_logic.middleware import add_tile_to_pygame
from noise_logic.generate_map import CreateNoiseGrid, BinarizedNoise, ColouredMap, CreateHeightReference
from matplotlib import pyplot as plt
import numpy as np
import pygame
import time

window_settings = {
    "width": 800,
    "height": 800
}

game = PygameInstance(width=window_settings["width"], height=window_settings["height"])

map_settings = {
    "size": 100,
    "scale": 0.01,
    "octaves": 8,
    "persistence": 0.5,
    "lacunarity": 2.0,
    "base": 22,
    "offset_x": 0,
    "offset_y": 0
}

height_reference = CreateHeightReference(map_settings["size"], 
                                map_settings["size"],
                                0.02,
                                map_settings["octaves"],
                                map_settings["persistence"],
                                map_settings["lacunarity"],
                                map_settings["base"],
                                map_settings["offset_x"],
                                map_settings["offset_y"]
                                )

min_and_max_height = height_reference.generate_height_reference()

def pollmap():

    map_object = CreateNoiseGrid(map_settings["size"], 
                                map_settings["size"],
                                map_settings["scale"],
                                map_settings["octaves"],
                                map_settings["persistence"],
                                map_settings["lacunarity"],
                                map_settings["base"],
                                map_settings["offset_x"],
                                map_settings["offset_y"]
                                )

    map = map_object.noise_grid

    binarized_map = BinarizedNoise(map, min_and_max_height[0], min_and_max_height[1]).apply()

    colored_map = ColouredMap(binarized_map).apply()

    return map, binarized_map, colored_map

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit()
            running = False

    game.clear_screen()

    map, binarized_map, colored_map = pollmap()

    time.sleep(0.01)

    map_settings["offset_x"] += 0.01
    map_settings["offset_y"] += 0.01

    start_x_pos = 100
    start_y_pos = 100
    tile_size = 4

    offset_x = tile_size + tile_size/2
    offset_y = tile_size + tile_size/2

    tile_widgets = []

    for y in range (map_settings["size"]):
        for x in range (map_settings["size"]):
            colour = colored_map[y][x]
            tile = add_tile_to_pygame(game.screen, colour, (start_x_pos + x * offset_x, start_y_pos + y * offset_y), tile_size)

            tile_widgets.append(tile)

    

    game.update_display()

pygame.quit()
