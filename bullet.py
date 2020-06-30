import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x+50,y+20)
        self.velocity = 10 * direction
    def move(self):
        self.rect.x = self.rect.x + self.velocity
