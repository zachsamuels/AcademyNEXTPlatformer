import sys
import os
import getopt
import pygame
pygame.init()


grass_tiles = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Terrain\Grass_Tileset.png')
ground_tiles = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_3.png')
background = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_2.png')
further_background = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\Grassland\Background\GrassLand_Background_1.png')

plat_top_left = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\GrassLand\Terrain\top_left.png')
plat_top_middle = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\GrassLand\Terrain\top_middle.png')
plat_top_right = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\GrassLand\Terrain\top_right.png')
plat_bottom_left = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\GrassLand\Terrain\bottom_left.png')
plat_bottom_middle = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\GrassLand\Terrain\bottom_middle.png')
plat_bottom_right = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\GrassLand\Terrain\bottom_right.png')
platform = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Multi_Platformer_Tileset_v2\GrassLand\Terrain\platform.png')

skeleton = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\2D Pixel Dungeon Asset Pack\character and tileset\skeleton.png')
cleric = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\2D Pixel Dungeon Asset Pack\character and tileset\cleric.png')
knight = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\2D Pixel Dungeon Asset Pack\character and tileset\knight.png')

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

idle = []
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle1.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle2.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle3.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle4.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle5.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle6.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle7.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle8.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle9.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle10.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle11.gif'))
idle.append(pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\sprite_art\Jungle Asset Pack\Character\sprites\idle12.gif'))


# in_air = pygame.image.load(r'C:\Users\Student\Documents\GitHub\AcademyNEXTPlatformer\Art\Jungle Asset Pack\Character\sprites\mid-air.gif')

pygame.display.init()
pygame.display.set_mode()

sky = (173, 216, 230) 
  
X = 820
Y = 480
X_pos = 0
left = False
right = False
chillCount = 0
  
display_surface = pygame.display.set_mode((X, Y )) 

def redrawGameWindow():
    global runCount
    global vspeed
    global airTicks
    global chillCount

    display_surface.fill(sky)
    display_surface.blit(further_background, (0, 0))
    display_surface.blit(background, (0, 0)) 
    display_surface.blit(ground_tiles, (0, 80))

    display_surface.blit(plat_top_left, (350, 0.75 * Y - 50))
    display_surface.blit(plat_top_middle, (375, 0.75 * Y - 50))
    display_surface.blit(plat_top_right, (400, 0.75 * Y - 50))
    display_surface.blit(plat_bottom_left, (350, 0.75 * Y - 25))
    display_surface.blit(plat_bottom_middle, (375, 0.75 * Y - 25))
    display_surface.blit(plat_bottom_right, (400, 0.75 * Y - 25))
    display_surface.blit(platform, (450, 0.75 * Y - 100))

    display_surface.blit(skeleton, (450, 0.75 * Y - 125))
    display_surface.blit(cleric, (480, 0.75 * Y - 125))
    display_surface.blit(knight, (510, 0.75 * Y - 125))

    if runCount + 1 >= 24:
        runCount = 0

    if airTicks + 1 >= 6:
        airTicks = 0

    if chillCount + 1 >= 36:
        chillCount = 0

    if not vspeed == 0:
        display_surface.blit(MidAir[airTicks//3], (40,325))
        airTicks += 1
    elif left:
        display_surface.blit(Run_left[runCount//3], (40,350))
        runCount += 1
    elif right:
        display_surface.blit(Run_right[runCount//3], (40,350))
        runCount += 1
    else:
        display_surface.blit(idle[chillCount//3], (40,350))
        chillCount += 1

    pygame.display.update()  



game = True
while game : 
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        vspeed = 4
        chillCount = 0
    else:
        vspeed = 0
        airTicks = 0

    if keys[pygame.K_LEFT]:
        left = True
        right = False
        chillCount = 0
    elif keys[pygame.K_RIGHT]:
        right = True
        left = False
        chillCount = 0
    else:
        left = False
        right = False
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