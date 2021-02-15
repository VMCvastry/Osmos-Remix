from interactions import *
from game_properties import Properties
from entities import Player
from menu import general_interactions_handler
from text import set_text
from constants import *


class Level:
    """
        general level superclass
        """
    def __init__(self, game: Properties):
        self.running = true
        self.player = Player
        self.enemies = []
        self.clicks = 0
        self.scale = 1
        self.time = 1
        self.won = false
        self.paused = false
        self.game = game
        self.level_init()

    def user_interaction_handler(self):
        """
                general user interaction pygame events handling
                """
        for event in pygame.event.get():
            if not general_interactions_handler(self.game, event):  # if quit==false
                return false
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = true
                if event.key == pygame.K_PLUS:  # just for debug
                    self.game.fps += 60
                    print(self.game.fps)
                if event.key == pygame.K_MINUS:  # just for debug
                    self.game.fps -= 60
                if event.key == pygame.K_w:  # time speed up
                    if self.time < 2:
                        self.time += 0.1
                        Sphere.time = self.time
                        text = set_text(str(round(self.time, 1)) + 'x', self.game.width // 2, self.game.height - 100,
                                        50)
                        self.game.screen.blit(text[0], text[1])
                if event.key == pygame.K_s:  # time speed down
                    if self.time > 0.6:
                        self.time -= 0.1
                        Sphere.time = self.time
                        text = set_text(str(round(self.time, 1)) + 'x', self.game.width // 2, self.game.height - 100,
                                        50)
                        self.game.screen.blit(text[0], text[1])
            if not self.paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # scroll up -> zoom in
                        if self.game.width / self.player.scaled_size() > 15:
                            self.scale += 0.1
                    if event.button == 5:
                        if self.scale > 0.1 and self.game.width / self.player.scaled_size() < 40:
                            self.scale -= 0.1
                    if event.button == 1:
                        self.clicks += 50  #TODO Fix
                        # x, y = pygame.mouse.get_pos()
                        # # print((x-player.x)/player.size,(y-player.y)/player.size)
                        # print(get_trig(x - player.pos()[0],y -  player.pos()[1]))
                        # print(get_trig(player))
                        self.enemies.append(
                            self.player.accelerate(trig=get_trig(self.player), power=self.clicks // 30))
                    Sphere.scale = self.scale  # updates sphere scale property according to the desired zoom level
        return true

    def level_init(self):
        return

    def run_level(self):
        return
