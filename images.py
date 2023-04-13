import pygame


class Image:
    def __init__(self):
        self.bg_image = pygame.image.load('graphics/background/background1.jpg').convert_alpha()
        self.letter_image = None
