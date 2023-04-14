import pygame
from os import listdir


class Image:
    def __init__(self):
        self.bg1_image = pygame.image.load('graphics/background/background1.jpg')
        self.bg2_image = pygame.image.load('graphics/background/background2.jpg')
        self.bacgrounds = [self.bg1_image, self.bg2_image]


    def convert_images(self):
        self.bg1_image.convert_alpha()
        self.bg2_image.convert_alpha()
