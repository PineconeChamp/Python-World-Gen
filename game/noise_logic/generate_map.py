import noise

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
        for i in range(len(self.noise_map)):
            for j in range(len(self.noise_map[i])):
                match self.noise_map[i][j]:
                    case p if p >= 0.9:
                        self.noise_map[i][j] = 1
                    case p if p >= 0.7:
                        self.noise_map[i][j] = 0.8
                    case p if p >= 0.5:
                        self.noise_map[i][j] = 0.7
                    case p if p >= 0.3:
                        self.noise_map[i][j] = 0.3
                    case p if p >= 0.1:
                        self.noise_map[i][j] = 0.3
                    case p if p >= 0:
                        self.noise_map[i][j] = 0.1
        return self.noise_map
