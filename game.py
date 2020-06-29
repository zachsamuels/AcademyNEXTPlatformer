import pygame
import random
from generator import Generator
from character import Character
from platform import Platform

#init pygame and create screen
pygame.init()
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

#create a list of things to call move function on...
#all platforms should be moved by a set amount left every time the game loop continues
platforms = []

#create an instance of the Generator class to create platforms and enemies
#given the width of the screen
PLATFORM_WIDTH, PLATFORM_HEIGHT = 150, 20
GENERATOR = Generator(WIDTH, HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)

#add basic platforms
platforms.append(Platform(0, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
platforms.append(Platform(300, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
character = Character()
#loop vars
counter = 0
last_platform_height = PLATFORM_HEIGHT
new_platform_mod = 250


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # add getting user input...

    for i in range(len(platforms)):
        try:
            if platforms[i].move():
                platforms.remove(platforms[i])
                i -= 1
        except:
            pass


    SCREEN.fill((255,255,255))
    character.update()



    #charecter collision

    #generate new platforms
    counter += 1
    if (counter % new_platform_mod == 0):
        platforms.append(GENERATOR.add_platform(last_platform_height))
        new_platform_mod = random.randint(200,450)
        counter = 0

    #blit platforms
    for o in platforms:
        SCREEN.blit(o.image, o.rect)
    SCREEN.blit(character.image, character.rect)



    pygame.display.flip()
