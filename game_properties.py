import pygame, random, math, colour
from constants import *
class Properties:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE| pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.fps = 144
        self.level=0