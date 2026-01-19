import noise_logic
import matplotlib.pyplot as plt
import numpy as np
from numpy import gradient
import pygame as pyg

scale = 0.05
octaves = 8
persistence = 0.5
lacunarity = 2.0

def create_noise_grid(width, height, scale, octaves, persistence, lacunarity):
    noise_grid = [
        [noise_logic.pnoise2(x * scale, y * scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=1024, repeaty=1024, base=42)
         for x in range(width)]
        for y in range(height)
    ]
    return noise_grid

def binarized_noise(noise_map):
    for i in range(len(noise_map)):
        for j in range(len(noise_map[i])):
            match noise_map[i][j]:
                case p if p >= 0.9:
                 noise_map[i][j] = 1
                case p if p >= 0.7:
                 noise_map[i][j] = 0.8
                case p if p >= 0.5:
                 noise_map[i][j] = 0.7
                case p if p >= 0.5:
                 noise_map[i][j] = 0.3
                case p if p >= 0.1:
                 noise_map[i][j] = 0.3
                case p if p >= 0:
                 noise_map[i][j] = 0.1
    return noise_map
