import pygame

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """ Initialize the game's settings."""
        pygame.init()
        self.info = pygame.display.Info()

        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        self.bg_color = (230, 230, 230)