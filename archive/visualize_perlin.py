#!/usr/bin/env python3
"""Tiny Perlin noise visualizer.

Run: python archive/visualize_perlin.py
Requires: pip install noise matplotlib numpy
"""
import numpy as np
import matplotlib.pyplot as plt

from game.noise_logic.generate_map import CreateNoiseGrid


def main():
    W, H = 200, 200
    grid = CreateNoiseGrid(W, H, scale=0.05, octaves=6, persistence=0.5, lacunarity=2.0)
    arr = np.array(grid.noise_grid)

    plt.figure(figsize=(6, 6))
    plt.imshow(arr, cmap="gray", origin="lower")
    plt.colorbar(label="noise")
    plt.title("Perlin noise")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
