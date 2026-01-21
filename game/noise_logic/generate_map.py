import noise
import math
import matplotlib.pyplot as plt
import numpy as np

#scale = 0.05
#octaves = 8
#persistence = 0.5
#lacunarity = 2.0

class CreateHeightReference:
    def __init__(self, width, height, scale, octaves, persistence, lacunarity, base=12, x_offset=0, y_offset=0):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.base = base
        self.x_offset = x_offset
        self.y_offset = y_offset

    def generate_height_reference(self):
        height_ref = [
        [noise.pnoise2(
            x * self.scale + self.x_offset,
            y * self.scale + self.y_offset,
            octaves=self.octaves,
            persistence=self.persistence,
            lacunarity=self.lacunarity,
            repeatx=1024, 
            repeaty=1024,
            base=self.base
            )

                for x in range(self.width)]
            for y in range(self.height)
        ]

        flattened_list = [v for row in height_ref for v in row]
        flattened_list.sort()

        max_value = flattened_list[-1]
        min_value = flattened_list[0]
        if min_value <= 0:
            min_value = 0.001

        print(max_value, min_value)

        #world = np.array(height_ref)

        #plt.figure(figsize=(6, 6))
        #plt.imshow(world, cmap="gray")
        #plt.colorbar(label="Noise value")
        #plt.title("2D Perlin Noise")
        #plt.axis("off")
        #plt.show()

        return [max_value, min_value]


class CreateNoiseGrid:

    def __init__(self, width, height, scale, octaves, persistence, lacunarity, base=12, x_offset=0, y_offset=0):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.base = base
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.noise_grid = self.generate_noise_grid()

    def generate_noise_grid(self):
        noise_grid = [
            [noise.pnoise2(
                x * self.scale + self.x_offset,
                y * self.scale + self.y_offset,
                octaves=self.octaves,
                persistence=self.persistence,
                lacunarity=self.lacunarity,
                repeatx=1024, repeaty=1024,
                base=self.base
                )

             for x in range(self.width)]
            for y in range(self.height)
        ]
        return noise_grid

class BinarizedNoise:
    def __init__(self, noise_map, maximum, minimum):
        self.noise_map = noise_map
        self.min_value = minimum
        self.max_value = maximum

    def apply(self):

        map_max = 1.0
        map_min = 0.0
        
        slope = (map_max - map_min) / (self.max_value - self.min_value)

        for i in range(len(self.noise_map)):
            for j in range(len(self.noise_map[i])):
                
                mapped_value = map_min + slope * (self.noise_map[i][j] - self.min_value)
                self.noise_map[i][j] = round(mapped_value, 1)
                
        return self.noise_map

class ColouredMap:
    def __init__(self, binarized_map):
        self.binarized_map = binarized_map

    def apply(self):
        for i in range(len(self.binarized_map)):
            for j in range(len(self.binarized_map[i])):
                match self.binarized_map[i][j]:
                    case 1:
                        self.binarized_map[i][j] = "#FFFFFF"
                    case 0.9:
                        self.binarized_map[i][j] = "#FFFFFF"
                    case 0.8:
                        self.binarized_map[i][j] = "#3D3833"
                    case 0.7:
                        self.binarized_map[i][j] = "#3D3833" 
                    case 0.6:
                        self.binarized_map[i][j] = "#3D3833"  
                    case 0.5:
                        self.binarized_map[i][j] = "#0B6112"
                    case 0.4:
                        self.binarized_map[i][j] = "#15831E"
                    case 0.3:
                        self.binarized_map[i][j] = "#E1BD6F"
                    case 0.2:
                        self.binarized_map[i][j] = "#6685E9"
                    case 0.1:
                        self.binarized_map[i][j] = "#6685E9"
                    case 0:
                        self.binarized_map[i][j] = "#526DC7"
                    case _:
                        self.binarized_map[i][j] = "#2E489C"
                    
        return self.binarized_map
