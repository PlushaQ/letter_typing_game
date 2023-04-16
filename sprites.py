import pygame
from random import randint

class Letter(pygame.sprite.Sprite):
    """ Class managing letters sprites and it's depencencies"""
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

    @classmethod
    def reset_speed(cls):
        cls.speed = 1

    def update(self, level):
        if level >= 5:
            self.shake()
        else:
            self.movement()
        
    def hit(self, key, score):
        if key.lower() == self.name.lower():
            self.kill()
            return score + 10
        return score
           

    def destroy(self):
        # Function to destroy sprite when it's not in the screen anymore
        if self.rect.y > 400 or self.rect.x < 0 or self.rect.x > 800:
            self.kill()
            return True


            

        