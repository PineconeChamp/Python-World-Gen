import pygame

class PygameInstance:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame Instance")
        self.bg_colour = pygame.Color("#526DC7")

    def clear_screen(self):
        self.screen.fill(self.bg_colour)

    def render(self):
        pass

    def update_display(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()