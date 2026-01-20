import pygame

class PygameInstance:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame Instance")

    def clear_screen(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def render(self):
        pass

    def update_display(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()