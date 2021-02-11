import pygame, random, math, colour
from interactions import *
from entities import *
from constants import *
from menu import *
from level0 import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class GameCore:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Osmos remix')
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.player=None
        self.enemies=[]
        # pygame.display.set_icon(icon)
        # self.running = true

    def main(self):
        while true:
            retry = level0(self)
            if not retry:
                break


if __name__ == '__main__':
    GameCore().main()
