import pygame
import os
import sys
from bullet import Bullet

class Character(pygame.sprite.Sprite):
    '''
    Character class that handles movement and user input
    '''
    Run_right = []
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run0.png')))
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run1.png')))
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run3.png')))
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run4.png')))
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run5.png')))
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run6.png')))
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run7.png')))
    Run_right.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run8.png')))

    Run_left = []
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run0.png')), True, False))
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run1.png')), True, False))
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run3.png')), True, False))
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run4.png')), True, False))
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run5.png')), True, False))
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run6.png')), True, False))
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run7.png')), True, False))
    Run_left.append(pygame.transform.flip(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run8.png')), True, False))

    MidAir = []
    MidAir.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','mid_air1.gif')))
    MidAir.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','mid_air2.gif')))

    idle = []
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle1.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle2.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle3.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle4.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle5.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle6.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle7.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle8.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle9.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle10.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle11.gif')))
    idle.append(pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','idle12.gif')))

    sky = (173, 216, 230) 
  
    X = 600
    Y = 600
    X_pos = 0
    left = False
    right = False
    chillCount = 0
    runCount = 0
    airTicks = 0

    def __init__(self, platforms, bullets):
        pygame.sprite.Sprite.__init__(self)
        self.image_png = pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run5.png'))
        self.image = pygame.transform.scale(self.image_png, (50,50))
        self.width, self.height = 50, 50
        self.rect = self.image.get_rect()
        self.rect.x += 50
        self.x = 0
        self.y = 0
        self.gravity = 9.8
        self.platforms = platforms
        self.bullets = bullets
        self.clock = pygame.time.Clock()
        self.jumping = False
        self.jump = 10
        self.hit = False
        self.can_jump = False

    def move(self, x, y):
        self.x += x
        self.y += y

    def redrawGameWindow(self):
        global runCount
        global vspeed
        global airTicks
        global chillCount

        if runCount + 1 >= 24:
            runCount = 0

        if airTicks + 1 >= 6:
            airTicks = 0

        if chillCount + 1 >= 36:
            chillCount = 0

        if self.jumping:
            self.image_png = MidAir[airTicks//3]
            airTicks += 1
        elif left_bool:
            self.image_png = Run_left[runCount//3]
            runCount += 1
        elif right_bool:
            self.image_png = Run_right[runCount//3]
            runCount += 1
        else:
            self.image_png = idle[chillCount//3]
            chillCount += 1

        self.image = pygame.transform.scale(self.image_png, (50,50))
        return self.image

    def update(self, tick):
        self.rect.x += self.x
        fitness = 0
        

        if self.jumping:
            if self.jump >= 0:
                self.rect.y -= (self.jump * abs(self.jump)) * 0.5
                self.jump -= 1
            else:
                self.jump = 10
                self.jumping = False

        if not any([pygame.sprite.collide_rect(self, platform) for platform in self.platforms]):
            self.rect.y += self.y + self.gravity
            self.can_jump = False
        else:
            for platform in self.platforms:
                if pygame.sprite.collide_rect(self, platform):
                    if self.rect.bottom > platform.rect.bottom:
                        self.rect.y += self.y + self.gravity
                        self.can_jump = False
                    else:
                        self.rect.y += self.y
                        self.jumping = False
                        self.can_jump = True
                        fitness += 2
        self.move_left(tick)
        if any([pygame.sprite.collide_rect(self, bullet) for bullet in self.bullets]):
            self.hit = True
        return fitness


    def move_left(self, tick):
        speed = .0589
        #clock = pygame.time.Clock()
        left = tick*speed
        self.rect.x = self.rect.x + left

    def shoot(self):
        return Bullet(self.rect.x, self.rect.y, 1)

    



if __name__ == "__main__":
    display = pygame.display.set_mode([400, 400])
    clock = pygame.time.Clock()
    character = Character()
    characters = pygame.sprite.Group()
    characters.add(character)
    while True:
        for e in pygame.event.get():
            if e.type is pygame.KEYDOWN:
                if e.key == ord('a'):
                    character.move(-10, 0)
                    left_bool = True
                    right_bool = False
                    chillCount = 0
                elif e.key == ord('d'):
                    character.move(10, 0)
                    right_bool = True
                    left_bool = False
                    chillCount = 0
                elif e.type is pygame.K_SPACE:
                    print("space")
                else:
                    left_bool = False
                    right_bool = False
                    runCount = 0
            if e.type is pygame.KEYUP:
                if e.key == ord('a'):
                    character.move(10, 0)
                    left_bool = False
                    right_bool = True
                    chillCount = 0
                elif e.key == ord('d'):
                    character.move(-10, 0)
                    left_bool = True
                    right_bool = False
                    chillCount = 0
                elif e.type is pygame.K_SPACE:
                    print("space")
                else:
                    left_bool = False
                    right_bool = False
                    runCount = 0

            if e.type is pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        character.image = redrawGameWindow()
        character.update()
        
        display.fill((25,25,200))
        characters.draw(display)
        pygame.display.flip()
        clock.tick(30)
