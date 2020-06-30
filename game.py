import pygame
import random
import sys
from generator import Generator
from character import Character
from platformclass import Platform
from enemy import Enemy

#init pygame and create screen
pygame.init()
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

#create a list of things to call move function on...
#all platforms should be moved by a set amount left every time the game loop continues
platforms = []
bullets = []

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
last_platform_height = 300
new_platform_mod = 75


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
            elif event.key == ord('s'):
                bullets.append(character.shoot())
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
            bullets.append(platforms[i].shoot())
        except:
            pass
    for bullet in bullets:
        bullet.move()

    SCREEN.fill((255,255,255))
    character.update()
    characters.draw(SCREEN)


    #charecter collision with bottom and left bound
    # if character.rect.y > HEIGHT:
    #     sys.exit()
    # if character.rect.x < 0:
    #     sys.exit()
    #generate new platforms
    counter += 1
    if (counter % new_platform_mod == 0):
        plat = GENERATOR.add_platform(last_platform_height)
        last_platform_height = plat.rect.y
        platforms.append(plat)
        new_platform_mod = random.randint(150,300)
        if random.randint(1,3) == 1:
            print(plat.rect.x)
            platforms.append(Enemy(plat.rect.x+100, plat.rect.y-50))
        counter = 0

    #blit platforms
    for o in platforms:
        SCREEN.blit(o.image, o.rect)
    for b in bullets:
        SCREEN.blit(b.image, b.rect)
    SCREEN.blit(character.image, character.rect)



    pygame.display.flip()
