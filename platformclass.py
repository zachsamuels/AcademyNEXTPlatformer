import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        #Create a temp image for the platform... will replace with sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(0)

        #creates a pygame rect to move
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)

    def move(self):
        #moves the rectanlge to the left and updates the rect variable
        speed = .1
        clock = pygame.time.Clock()
        left = -clock.tick(60)*speed
        self.x += left
        if (self.x+left+self.width < 0):
            return True
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
