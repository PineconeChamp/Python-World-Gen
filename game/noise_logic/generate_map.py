import noise
import math

#scale = 0.05
#octaves = 8
#persistence = 0.5
#lacunarity = 2.0

class CreateNoiseGrid:

    def __init__(self, width, height, scale, octaves, persistence, lacunarity):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.noise_grid = self.generate_noise_grid()

    def generate_noise_grid(self):
        noise_grid = [
            [noise.pnoise2(x * self.scale, y * self.scale, octaves=self.octaves, persistence=self.persistence, lacunarity=self.lacunarity, repeatx=1024, repeaty=1024, base=42)
             for x in range(self.width)]
            for y in range(self.height)
        ]
        return noise_grid

class BinarizedNoise:
    def __init__(self, noise_map):
        self.noise_map = noise_map

    def apply(self):
        flattened_list = [v for row in self.noise_map for v in row]
        sortvalues = flattened_list.copy()
        sortvalues.sort()

        max_value = sortvalues[-1]
        min_value = sortvalues[0]

        print(max_value, min_value)

        map_max = 1.0
        map_min = 0.0
        
        slope = (map_max - map_min) / (max_value - min_value)

        for i in range(len(self.noise_map)):
            for j in range(len(self.noise_map[i])):
                
                mapped_value = map_min + slope * (self.noise_map[i][j] - min_value)
                self.noise_map[i][j] = round(mapped_value, 1)
                print(round(mapped_value, 1))
                
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
                        self.binarized_map[i][j] = "#22A82D"
                    case 0.2:
                        self.binarized_map[i][j] = "#E9B066"
                    case 0.1:
                        self.binarized_map[i][j] = "#6685E9"
                    case 0:
                        self.binarized_map[i][j] = "#2E489C"
                    case _:
                        self.binarized_map[i][j] = "#2E489C"
                    
        return self.binarized_map
