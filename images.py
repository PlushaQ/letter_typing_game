import pygame
from os import listdir


class Image:
    """ Class to manage images"""
    def __init__(self):
        self.bg1_image = pygame.image.load('graphics/background/background1.jpg')
        self.bg2_image = pygame.image.load('graphics/background/background2.jpg')
        self.bacgrounds = [self.bg1_image, self.bg2_image]
        self.intro_bg = pygame.image.load('graphics/background/intro.jpg')


    def convert_images(self):
        self.bg1_image.convert_alpha()
        self.bg2_image.convert_alpha()
        self.intro_bg.convert_alpha()