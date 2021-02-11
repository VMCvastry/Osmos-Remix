import pygame, random, math, colour
from interactions import *
from entities import *
from constants import *
from menu import *
from structures import *


class Level2(Level):

    def __init__(self, game: Properties):
        super().__init__(game)

    def level_init(self):
        self.player = Player(20, random.randint(20, game_width - 20), random.randint(20, game_height - 20))
        # self.player = Player(200, 400, 400)

        self.enemies = [
            Sphere(random.randint(2, 20), random.randint(20, game_width - 20), random.randint(20, game_height - 20)) for
            x in
            range(100)]
        # self.enemies.append(Sphere(150, 700,400))
        # for enemy in self.enemies:
        #     enemy.speed(random.randint(-1, 1) / 1, random.randint(-1, 1) / 1)

    def run_level(self):
        # level0_init(self)
        # running = true
        # player = None
        # enemies = []
        # clicks = 0
        # scale = 1
        # won=false
        # paused = false
        while self.running:
            self.game.screen.fill((0, 0, 255))
            # self.screen.blit(background, (0, 0))
            ratio = (width / game_width) * self.scale
            # self.screen.blit(pygame.transform.scale(background, (game_width, game_height)), (round(-player.x*(width/game_width)*scale), round(-player.y*(width/game_width))*scale))
            self.game.screen.blit(
                pygame.transform.scale(background, (round(game_width * self.scale), round(game_height * self.scale))),
                (round(-(self.player.x * self.scale - self.player.pos()[0])),
                 round(-(self.player.y * self.scale - self.player.pos()[1]))))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.level = -1
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = true
                    if event.key == pygame.K_PLUS:
                        self.game.fps += 60
                        print(self.game.fps)
                    if event.key == pygame.K_MINUS:
                        self.game.fps -= 60
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
            if self.clicks > 0:
                self.clicks -= 1
            # print(clicks)
            if not self.paused:
                if self.player.size < 1:
                    return game_over(self.game)
                pygame.draw.circle(self.game.screen, (0, 255, 255), self.player.pos(), self.player.scaled_size())
                self.player.update()
                # print(player.speed_x,player.speed_y)
                for enemy in self.enemies.copy():
                    pygame.draw.circle(self.game.screen, enemy.color, enemy.pos(), enemy.scaled_size())
                    if not enemy.update():
                        self.enemies.remove(enemy)
                for enemy in self.enemies + [self.player]:
                    for enemy2 in self.enemies + [self.player]:
                        if enemy2 != enemy:
                            if collision(enemy, enemy2):
                                attack(enemy, enemy2)
                pygame.draw.circle(self.game.screen, (150, 150, 150),
                                   [pos + (self.player.scaled_size() * 1.5) * dir for pos, dir in
                                    zip(self.player.pos(), get_trig(self.player))], 5)
                # self.screen.blit(pointer,[pos + (player.scaled_size() * 1.5) * dir for pos, dir in
                #                     zip(player.pos(), get_trig(player))])
                if all([self.player.size > enemy.size for enemy in self.enemies]) and not self.won:
                    self.won = true
                    self.paused = true
            else:
                if self.won:
                    if not pause_menu(self.game, won=true):
                        return false
                    else:
                        self.paused=false
                else:
                    if not pause_menu(self.game):
                        return false
                    else:
                        self.paused=false

            pygame.display.update()
            self.game.clock.tick(self.game.fps)
