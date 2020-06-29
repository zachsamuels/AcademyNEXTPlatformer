import sys
import os
import getopt
import pygame
pygame.init()


grass_tiles = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Terrain\Grassland_Terrain_Tileset.png')
ground_tiles = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_3.png')
background = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_2.png')
further_background = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_1.png')

Run_right = []
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run0.png'))
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run1.png'))
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run3.png'))
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run4.png'))
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run5.png'))
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run6.png'))
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run7.png'))
Run_right.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run8.png'))

Run_left = []
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run0.png'), True, False))
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run1.png'), True, False))
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run3.png'), True, False))
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run4.png'), True, False))
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run5.png'), True, False))
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run6.png'), True, False))
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run7.png'), True, False))
Run_left.append(pygame.transform.flip(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\run8.png'), True, False))

MidAir = []
MidAir.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\mid_air1.gif'))
MidAir.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\mid_air2.gif'))


# in_air = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\mid-air.gif')

pygame.display.init()
pygame.display.set_mode()

sky = (173, 216, 230) 
  
X = 785
Y = 400
X_pos = 0
left = False
right = False
  
display_surface = pygame.display.set_mode((X, Y )) 

def redrawGameWindow():
    global runCount
    display_surface.fill(sky)
    display_surface.blit(further_background, (0, 0.5 * Y))
    display_surface.blit(background, (0, 0.5 * Y)) 
    display_surface.blit(ground_tiles, (0, 0.5 * Y))

    if runCount + 1 >= 24:
        runCount = 0

    if left:
        display_surface.blit(Run_left[runCount//3], (40,40))
        runCount += 1
    elif right:
        display_surface.blit(Run_right[runCount//3], (40,40))
        runCount +=1
    else:
        display_surface.blit(Run_right[0], (40,40))

    pygame.display.update()  



game = True
while game : 
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    
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