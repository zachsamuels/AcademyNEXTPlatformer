import pygame
from platform import Platform
import random

class Generator:
    def __init__(self, max_x, width, height):
        #declares the desired width and height of platforms as well as the x cord of where they should spawn
        self.width, self.height = width, height
        self.max_x = max_x
    def add_platform(self, last_platform_height):
        #creates a platform object given the last_platform_height adn returns it to be added to the list
        height_dif = random.randint(-200,50)
        if last_platform_height-height_dif < 0:
            height_dif = 0
        return Platform(self.max_x, last_platform_height-height_dif, self.width, self.height)
