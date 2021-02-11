import pygame, random, math, colour
from interactions import *
from entities import *
from constants import *
from menu import *
from level1 import *
from level2 import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class GameCore:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Osmos remix')
        # self.screen = pygame.display.set_mode((width, height))
        #
        # self.clock = pygame.time.Clock()
        # self.fps = 60
        self.game=Properties()
        # self.player=None
        # self.enemies=[]
        # pygame.display.set_icon(icon)
        # self.running = true


    def main(self):
        while self.game.level!=-1:
            if self.game.level==1:
                Level1(self.game).run_level()
            elif self.game.level==2:
                Level2(self.game).run_level()
            elif self.game.level==0:
                main_menu(self.game)



if __name__ == '__main__':
    GameCore().main()
