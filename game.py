import pygame
import random
import sys
import os
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
enemies = []

#create an instance of the Generator class to create platforms and enemies
#given the width of the screen
PLATFORM_WIDTH, PLATFORM_HEIGHT = 150, 20
GENERATOR = Generator(WIDTH, HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)

#simple bg art
X = 600
Y = 600
ground_tiles = pygame.image.load(os.path.join('sprite_art','Multi_Platformer_Tileset_v2','Grassland','Background','GrassLand_Background_3.png'))
background = pygame.image.load(os.path.join('sprite_art','Multi_Platformer_Tileset_v2','Grassland','Background','GrassLand_Background_2.png'))
further_background = pygame.image.load(os.path.join('sprite_art','Multi_Platformer_Tileset_v2','Grassland','Background','GrassLand_Background_1.png'))
sky = (173, 216, 230)

#add basic platforms
platforms.append(Platform(0, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
platforms.append(Platform(300, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
character = Character(platforms, bullets)
characters = pygame.sprite.Group()
characters.add(character)

#loop vars
counter = 0
last_platform_height = 300
new_platform_mod = 15
bullet_counter = 0
score = 0
bullet_cooldown = 25
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type is pygame.KEYDOWN:
            elif event.key == ord('w'):
                if not character.jumping and character.can_jump:
                    character.jumping = True
            # elif event.key == ord('s'):
            #     if bullet_cooldown > 25:
            #         bullets.append(character.shoot())
            #         bullet_cooldown = 0
        #if event.type is pygame.KEYUP:
        #    if event.key == ord('a'):
        #        character.move(10, 0)
        #    elif event.key == ord('d'):
        #        character.move(-10, 0)

    bullet_counter += 1
    bullet_cooldown += 1
    tick = clock.tick(30)
    for i in range(len(platforms)):
        try:
            if platforms[i].move(tick):
                platforms.remove(platforms[i])
                i -= 1
        except:
            pass
    for i in range(len(bullets)):
        try:
            bullets[i].move()
            if bullets[i].rect.x > WIDTH or bullets[i].rect.x < 0:
                bullets.remove(bullets[i])
                i -= 1
        except:
            pass
    for enemy in enemies:
        enemy.move(tick)
        if bullet_counter % 100 == 0:
            bullets.append(enemy.shoot())
    SCREEN.fill(sky)
    SCREEN.blit(further_background, (0, Y - 520))
    SCREEN.blit(background, (0, Y - 460))
    SCREEN.blit(ground_tiles, (0, Y - 400))
    character.update(tick)
    characters.draw(SCREEN)
    for i in range(len(enemies)):
        try:
            if any([pygame.sprite.collide_rect(enemies[i], bullet) for bullet in bullets]):
                enemies.remove(enemies[i])
                score += 25
                i -=1
            elif enemies[i].rect.x < 0:
                enemies.remove(enemies[i])
        except:
            pass
    # charecter collision with bottom and left bound
    if character.rect.y > HEIGHT:
        sys.exit()
    if character.rect.x < 0:
        sys.exit()
    #generate new platforms
    counter += 1
    if (counter % new_platform_mod == 0):
        plat = GENERATOR.add_platform(last_platform_height)
        last_platform_height = plat.rect.y
        platforms.append(plat)
        new_platform_mod = random.randint(50,80)
        if random.randint(1,2) == 1:
            print(plat.rect.x)
            enemies.append(Enemy(plat.rect.x+100, plat.rect.y-50))
        counter = 0
        score += 50
        print(score)

    #blit platforms
    for o in platforms:
        SCREEN.blit(o.image, o.rect)
    for b in bullets:
        SCREEN.blit(b.image, b.rect)
    # for e in enemies:
    #     SCREEN.blit(e.image, e.rect)
    SCREEN.blit(character.image, character.rect)



    pygame.display.flip()

