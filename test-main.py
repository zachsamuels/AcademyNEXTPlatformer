import pygame
import random
from platformclass import Platform
from generator import Generator
from character import Character

pygame.init()

screen = pygame.display.set_mode([600,600])
platform = Platform(500, 300, 150, 20)

platforms = []
platforms.append(platform)


running = True
counter = 100

#pass in platforms max x, width, and height
g = Generator(600, 600, 150, 20)
last_platform_height = 200
new_platform_mod = 250
character = Character(platforms)
characters = pygame.sprite.Group()
characters.add(character)
while running:
    for e in pygame.event.get():
        if e.type is pygame.KEYDOWN:
            if e.key == ord('a'):
                character.move(-10, 0)
            elif e.key == ord('d'):
                character.move(10, 0)
            elif e.type is pygame.K_SPACE:
                print("space")
        if e.type is pygame.KEYUP:
            if e.key == ord('a'):
                character.move(10, 0)
            elif e.key == ord('d'):
                character.move(-10, 0)
            elif e.type is pygame.K_SPACE:
                print("space")
        if e.type == pygame.QUIT:
            running = False

    for i in range(len(platforms)):
        #checks if platform is off screen and removes it from the list if it is
        try:
            if platforms[i].move():
                platforms.remove(platforms[i])
                print(len(platforms))
                i -= 1
        except:
            pass
    screen.fill((255,255,255))

    for o in platforms:
        screen.blit(o.image, o.rect)

    counter += 1


    if counter % new_platform_mod == 0:
        platforms.append(g.add_platform(last_platform_height))
        print(new_platform_mod)
        new_platform_mod = random.randint(200, 450)
        counter = 0

    character.update()
    characters.draw(screen)
    
    pygame.display.flip()
