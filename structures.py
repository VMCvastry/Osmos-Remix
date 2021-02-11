import pygame, random, math, colour
from interactions import *
from entities import *
from constants import *
from menu import *
class Properties:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.level=0




class Level:
    def __init__(self,game:Properties):
        self.running = true
        self.player = Player
        self.enemies = []
        self.clicks = 0
        self.scale = 1
        self.won=false
        self.paused = false
        self.game=game
        self.level_init()

    def level_init(self):
        return

    def run_level(self):
        return
