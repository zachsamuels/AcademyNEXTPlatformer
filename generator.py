import pygame
from platformclass import Platform
import random

class Generator:
    def __init__(self, max_x, max_y, width, height):
        #declares the desired width and height of platforms as well as the x cord of where they should spawn
        self.width, self.height = width, height
        self.max_x = max_x + 200
        self.max_y = max_y
    def add_platform(self, last_platform_height):
        #creates a platform object given the last_platform_height adn returns it to be added to the list
        height_dif = random.randint(-50,50)
        if last_platform_height+height_dif < 0 or last_platform_height-height_dif > self.max_y:
            height_dif = 0
        return Platform(self.max_x, last_platform_height+height_dif, self.width, self.height)
