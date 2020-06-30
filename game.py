import pygame
import random
import sys
from generator import Generator
from character import Character
from platformclass import Platform

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
character = Character(platforms)
characters = pygame.sprite.Group()
characters.add(character)

#loop vars
counter = 0
last_platform_height = PLATFORM_HEIGHT
new_platform_mod = 250


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type is pygame.KEYDOWN:
            if event.key == ord('a'):
                character.move(-10, 0)
            elif event.key == ord('d'):
                character.move(10, 0)
            elif event.key == ord('w'):
                print("jump")
        if event.type is pygame.KEYUP:
            if event.key == ord('a'):
                character.move(10, 0)
            elif event.key == ord('d'):
                character.move(-10, 0)


    for i in range(len(platforms)):
        try:
            if platforms[i].move():
                platforms.remove(platforms[i])
                i -= 1
        except:
            pass


    SCREEN.fill((255,255,255))
    character.update()
    characters.draw(SCREEN)


    #charecter collision with bottom and left bound
    if character.rect.y > HEIGHT:
        sys.exit()
    if character.rect.x < 0:
        sys.exit()
    #generate new platforms
    counter += 1
    if (counter % new_platform_mod == 0):
        platforms.append(GENERATOR.add_platform(last_platform_height))
        new_platform_mod = random.randint(150,300)
        counter = 0

    #blit platforms
    for o in platforms:
        SCREEN.blit(o.image, o.rect)
    SCREEN.blit(character.image, character.rect)



    pygame.display.flip()
