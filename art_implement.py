import sys
import os
import getopt
import pygame
pygame.init()


grass_tiles = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Multi_Platformer_Tileset_v2\Grassland\Terrain\Grassland_Terrain_Tileset.png')
ground_tiles = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_3.png')
background = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_2.png')
further_background = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_1.png')

Run = []

Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_0_delay-0.1s.png'))
Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_1_delay-0.1s.png'))
Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_2_delay-0.1s.png'))
Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_3_delay-0.1s.png'))
Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_4_delay-0.1s.png'))
Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_5_delay-0.1s.png'))
Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_6_delay-0.1s.png'))
Run.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\Run\frame_7_delay-0.1s.png'))

in_air = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\mid-air.gif')

pygame.display.init()
pygame.display.set_mode()

sky = (173, 216, 230) 
  
X = 785
Y = 400
X_pos = 0

  
display_surface = pygame.display.set_mode((X, Y )) 

def redrawGameWindow():
    global runCount
    display_surface.fill(sky)
    display_surface.blit(further_background, (0, 0.5 * Y))
    display_surface.blit(background, (0, 0.5 * Y)) 
    display_surface.blit(ground_tiles, (0, 0.5 * Y))

    if runCount + 1 >= 27:
        runCount = 0

    if run_bool:
        display_surface.blit(Run[runCount//3], (40,40))
        runCount += 1
    pygame.display.update()  



game = True
while game : 
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    
    run_bool = True
    if keys[pygame.K_LEFT]:
        left = True
        right = False
    elif keys[pygame.K_RIGHT]:
        right = True
        left = False
    else:
        runCount = 0
    # if run_bool == True:
        # runCount = runCount += 1

    #for i in range(X // 200 - 1) :
        
        #display_surface.blit(further_background, (X_pos, 0.5 * Y))
        #display_surface.blit(background, (X_pos, 0.5 * Y)) 
        #display_surface.blit(ground_tiles, (X_pos, 0.5 * Y))
        #X_pos += 200

    # if player_Y < 160:
    # for i in range(8) :
        # display_surface.blit(Run[i], (30, Y-50))
        # pygame.display.update() 

    redrawGameWindow()

pygame.quit() 