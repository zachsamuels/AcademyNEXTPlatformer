import pygame
import random
import sys
from generator import Generator
from character import Character
from platformclass import Platform
from enemy import Enemy
import neat
import os

#init pygame and create screen
pygame.init()
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

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
    platforms = []
    bullets = []
    
    platforms.append(Platform(0, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    platforms.append(Platform(300, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    nets = []
    ge = []
    characters = []
    characterz = pygame.sprite.Group()
    for g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g[1], config)
        nets.append(net)
        char = Character(platforms, bullets)
        characters.append(char)
        characterz.add(char)
        g[1].fitness = 0
        ge.append(g[1])



    #loop vars
    counter = 0
    last_platform_height = 300
    new_platform_mod = 15
    score = 0
    clock = pygame.time.Clock()

    while running:

        tick = clock.tick(30)
        for i in range(len(platforms)):
            try:
                if platforms[i].move(tick):
                    platforms.remove(platforms[i])
                    i -= 1
            except:
                pass

        SCREEN.fill(sky)
        SCREEN.blit(further_background, (0, Y - 520))
        SCREEN.blit(background, (0, Y - 460))
        SCREEN.blit(ground_tiles, (0, Y - 400))
        

        #generate new platforms
        counter += 1
        if (counter % new_platform_mod == 0):
            plat = GENERATOR.add_platform(last_platform_height)
            last_platform_height = plat.rect.y
            platforms.append(plat)
            new_platform_mod = random.randint(50,80)
            counter = 0
            score += 1
            for g in ge:
                g.fitness += 5
            print(score)

        #blit platforms
        for o in platforms:
            SCREEN.blit(o.image, o.rect)
        
        for i, character in enumerate(characters):
            character.update()
            
            if character.rect.y > HEIGHT or character.rect.x < 0:
                ge[i].fitness -=1
                characters.pop(i)
                nets.pop(i)
                ge.pop(i)

            SCREEN.blit(character.image, character.rect)

        characterz.draw(SCREEN)
        pygame.display.flip()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultSpeciesSet, config_path)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)