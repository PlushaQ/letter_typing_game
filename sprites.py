import pygame
from random import randint

class Letter(pygame.sprite.Sprite):
    speed = 1
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(f'graphics/letters/{name}.png').convert_alpha()
        self.x_pos = 0
        self.direction = 1
        self.rotation_angle = 0
        self.rect = self.image.get_rect(midbottom=(randint(50, 750), randint(-100, 0 )))
        self.speed = Letter.speed

    def movement(self):
        self.rect.y += self.speed

    def shake(self):
        self.rect.y += self.speed
        self.rect.x += randint(-10, 10)
    
    @classmethod
    def increase_speed(cls):
        cls.speed += 1
        print(cls.speed)

    def update(self, level):
        if level >= 5:
            self.shake()
        else:
            self.movement()
        self.rect.y += 0
        self.destroy()

    def destroy(self):
        # Function to destroy sprite when it's not in the screen anymore
        if self.rect.y > 400:
            self.kill()