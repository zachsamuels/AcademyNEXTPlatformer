import pygame
import random
from generator import Generator
from character import Character
from platformclass import Platform

#init pygame and create screen
pygame.init()
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

#create a list of things to call move function on...
#all sprites should be moved by a set amount left every time the game loop continues
sprites = []

#create an instance of the Generator class to create platforms and enemies
#given the width of the screen
PLATFORM_WIDTH, PLATFORM_HEIGHT = 150, 20
GENERATOR = Generator(WIDTH, HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)

#add basic platforms
sprites.append(Platform(0, 300, PLATFORM_HEIGHT, PLATFORM_WIDTH))
sprites.append(Platform(300, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
character = Character(sprites)
#loop vars
counter = 0
last_platform_height = PLATFORM_HEIGHT


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # add getting user input...
    '''
    for i in range(len(sprites)):
        try:
            if sprites[i].move():
                sprites.remove(sprites[i])
                i -= 1
        except:
            pass
    '''

    SCREEN.fill((255,255,255))
    character.update()



    #charecter collision


    #generate new platforms


    #blit sprites
    for o in sprites:
        SCREEN.blit(o.image, o.rect)
    SCREEN.blit(character.image, character.rect)



    pygame.display.flip()
