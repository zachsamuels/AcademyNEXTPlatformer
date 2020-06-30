import pygame
import os
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = 50, 50

        image = pygame.image.load(os.path.join('images', 'character.png'))
        self.image = pygame.transform.scale(image, (50,50))
        self.image = pygame.transform.flip(self.image, True, False)
        self.width, self.height = 50, 50
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(x, y)

    def shoot(self):
        return Bullet(self.rect.x-60, self.rect.y, -1)
    def move(self):
        #moves the rectanlge to the left and updates the rect variable
        speed = .005
        clock = pygame.time.Clock()
        left = -clock.tick(60)*speed
        self.rect.x = self.rect.x + left
        if (self.rect.x+left+self.width < 0):
            return True
