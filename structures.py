import pygame, random, math, colour
from interactions import *
from entities import *
from constants import *
# from constants  import width,height
from menu import *

class Properties:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE| pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.fps = 144
        self.level=0

def general_interactions_handler(game,event):
    if event.type == pygame.QUIT:
        game.level = -1
        return false
    elif event.type == pygame.VIDEORESIZE:
        new_size = event.dict['size']
        global width, height
        print(new_size)
        width, height = new_size
        if width < 1200:
            width = 1200
        if height < 800:
            height = 800
        game.screen=pygame.display.set_mode((width, height), pygame.RESIZABLE| pygame.HWSURFACE | pygame.DOUBLEBUF)
    return true


class Level:
    def __init__(self,game:Properties):
        self.running = true
        self.player = Player
        self.enemies = []
        self.clicks = 0
        self.scale = 1
        self.time=1
        self.won=false
        self.paused = false
        self.game=game
        self.level_init()

    def user_interaction_handler(self):
        for event in pygame.event.get():
            if not general_interactions_handler(self.game,event):
                return false
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = true
                if event.key == pygame.K_PLUS:
                    self.game.fps += 60
                    print(self.game.fps)
                if event.key == pygame.K_MINUS:
                    self.game.fps -= 60
                if event.key == pygame.K_w:
                    if self.time<2:
                        self.time += 0.1
                        Sphere.time = self.time
                        text = set_text(str(round(self.time,1))+'x', width // 2, height-100, 50)
                        self.game.screen.blit(text[0], text[1])
                if event.key == pygame.K_s:
                    if self.time >0.6:
                        self.time -= 0.1
                        Sphere.time = self.time
                        text = set_text(str(round(self.time, 1)) + 'x', width // 2, height - 100, 50)
                        self.game.screen.blit(text[0], text[1])
            if not self.paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if width / self.player.scaled_size() > 15:
                            self.scale += 0.1
                    if event.button == 5:
                        if self.scale > 0.1 and width / self.player.scaled_size() < 40:
                            self.scale -= 0.1
                    if event.button == 1:
                        self.clicks += 50
                        # x, y = pygame.mouse.get_pos()
                        # # print((x-player.x)/player.size,(y-player.y)/player.size)
                        # print(get_trig(x - player.pos()[0],y -  player.pos()[1]))
                        # print(get_trig(player))
                        self.enemies.append(
                            self.player.accelerate(get_trig(self.player), self.clicks // 30))

                    Sphere.scale = self.scale
        return  true
    def level_init(self):
        return

    def run_level(self):
        return
