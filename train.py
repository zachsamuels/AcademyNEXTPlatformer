import pygame
import random
import sys
from generator import Generator
from character import Character
from platformclass import Platform
from enemy import Enemy
import neat
import os
import numpy as np
import pickle

#init pygame and create screen
pygame.init()
WIDTH, HEIGHT = 875, 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])


#create a list of things to call move function on...
#all platforms should be moved by a set amount left every time the game loop continues


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
def main(genomes, config):
    running = True
    platforms = []
    bullets = []
    enemies = []

    platforms.append(Platform(0, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    platforms.append(Platform(300, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    platforms.append(Platform(600, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    #platforms.append(Platform(800, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    nets = []
    ge = []
    characters = []
    bullet_counter = 0

    for g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g[1], config)
        nets.append(net)
        char = Character(platforms, bullets)
        characters.append(char)
        g[1].fitness = 0
        ge.append(g[1])



    #loop vars
    counter = 0
    last_platform_height = 300
    new_platform_mod = 15
    score = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        if not len(characters):
            running = False
            break

        tick = clock.tick(30)
        for i in range(len(platforms)):
            try:
                if platforms[i].move(tick):
                    platforms.remove(platforms[i])
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


        #generate new platforms
        counter += 1
        bullet_counter += 1
        if (counter % new_platform_mod == 0):
            plat = GENERATOR.add_platform(last_platform_height)
            last_platform_height = plat.rect.y
            platforms.append(plat)
            new_platform_mod = random.randint(50, 100)
            counter = 0
            score += 1
            print(score)
            if random.randint(1,3) == 1:
                print('new enemy')
                enemies.append(Enemy(plat.rect.x+100, plat.rect.y-50))

        #blit platforms
        for o in platforms:
            SCREEN.blit(o.image, o.rect)
        for enemy in enemies:
            SCREEN.blit(enemy.image, enemy.rect)
        for bullet in bullets:
            SCREEN.blit(bullet.image, bullet.rect)

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


        for i, character in enumerate(characters):
            #ge[i].fitness += character.rect.x / 200
            p_index = 0
            for p in platforms:
                if character.rect.x > p.rect.left:
                    p_index += 1
                    #ge[i].fitness += 1
                else:
                    break

            ge[i].fitness += .01

            b_index = 0
            for b in bullets:
                if character.rect.x > b.rect.left:
                    b_index += 1
                else:
                    break
            
            e_index = 0
            for e in enemies:
                if character.rect.x > e.rect.left:
                    e_index += 1
                else:
                    break

            try:
                output = nets[i].activate((character.rect.x, character.rect.y, platforms[p_index-1].rect.left, platforms[p_index-1].rect.right, platforms[p_index-1].rect.y, platforms[p_index].rect.left, platforms[p_index].rect.right, platforms[p_index].rect.y, bullets[b_index].rect.x, bullets[b_index].rect.x, enemies[e_index].rect.x, enemies[e_index].rect.y, 875 - character.rect.x))
            except:
                try:
                    output = nets[i].activate((character.rect.x, character.rect.y, platforms[p_index-2].rect.left, platforms[p_index-2].rect.right, platforms[p_index-2].rect.y, platforms[p_index-1].rect.left, platforms[p_index-1].rect.right, platforms[p_index-1].rect.y, 0, 0, enemies[e_index].rect.x, enemies[e_index].rect.y, 875 - character.rect.x))
                except:
                    output = nets[i].activate((character.rect.x, character.rect.y, platforms[p_index-2].rect.left, platforms[p_index-2].rect.right, platforms[p_index-2].rect.y, platforms[p_index-1].rect.left, platforms[p_index-1].rect.right, platforms[p_index-1].rect.y, 0, 0, 0, 0, 875 - character.rect.x))

            soft = neat.math_util.softmax(output)
            class_output = np.argmax(((soft / np.max(soft)) == 1).astype(int))

            #print(class_output)
            if not class_output:
                character.left_bool = False
                character.right_bool = True
                pass
            elif class_output == 1:
                character.move(10, 0)
                character.left_bool = False
                character.right_bool = True
                character.chillCount = 0
            elif class_output == 2:
                character.move(-10, 0)
                character.left_bool = True
                character.right_bool = False
                character.chillCount = 0
            else:
                if not character.jumping and character.can_jump:
                    character.jumping = True
                    character.chillCount = 0
                else:
                    character.left_bool = False
                    character.right_bool = False
                    character.runCount = 0


            ge[i].fitness += character.update(tick)

            if character.rect.y > HEIGHT:
                ge[i].fitness -= 1
                char = characters.pop(i)
                nets.pop(i)
                ge.pop(i)
                continue

            if character.rect.x > 825:
                ge[i].fitness -=.1
                character.rect.x = 875 - character.width

            if character.rect.x == 0:
                ge[i].fitness -=5
                char = characters.pop(i)
                nets.pop(i)
                ge.pop(i)
                continue

            if character.hit:
                ge[i].fitness -= 1
                char = characters.pop(i)
                nets.pop(i)
                ge.pop(i)
                continue

            character.redrawGameWindow()
            SCREEN.blit(character.image, character.rect)

        pygame.display.flip()

def run(config_path):
    
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 100)
    pickle.dump(winner, open("winner.p", "wb"))
    '''
    with open('winner.p', "rb") as f:
        genome = pickle.load(f)

    # Convert loaded genome into required data structure
    genomes = [(1, genome)]

    # Call game with only the loaded genome
    main(genomes, config)
    '''
    



if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
