import pygame, random, math, colour
from interactions import *
from entities import *
from constants import *
from menu import *
from main import *


def level0_init(self: GameCore):

    self.player = Player(20, random.randint(20, game_width-20), random.randint(20, game_height-20))
    # self.player = Player(200, 400, 400)

    self.enemies = [Sphere(random.randint(2, 20), random.randint(20, game_width-20),random.randint(20, game_height-20)) for
                    x in
                    range(100)]
    # self.enemies.append(Sphere(150, 700,400))
    # for enemy in self.enemies:
    #     enemy.speed(random.randint(-1, 1) / 1, random.randint(-1, 1) / 1)


def level0(self: GameCore):
    level0_init(self)
    running = true
    player = self.player
    enemies = self.enemies
    clicks = 0
    scale = 1
    won=false
    self.paused = false
    while running:
        self.screen.fill((0, 0, 255))
        # self.screen.blit(background, (0, 0))
        ratio = (width / game_width) * scale
        # self.screen.blit(pygame.transform.scale(background, (game_width, game_height)), (round(-player.x*(width/game_width)*scale), round(-player.y*(width/game_width))*scale))
        self.screen.blit(
            pygame.transform.scale(background, (round(game_width * scale), round(game_height * scale))),
            (round(-(player.x * scale - player.pos()[0])), round(-(player.y * scale - player.pos()[1]))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return false
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = true
                if event.key == pygame.K_PLUS:
                    self.fps += 60
                    print(self.fps)
                if event.key == pygame.K_MINUS:
                    self.fps -= 60
            if not self.paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if width / player.scaled_size() > 15:
                            scale += 0.1
                    if event.button == 5:
                        if scale > 0.1 and width / player.scaled_size() < 40:
                            scale -= 0.1
                    if event.button == 1:
                        clicks += 50
                        # x, y = pygame.mouse.get_pos()
                        # # print((x-player.x)/player.size,(y-player.y)/player.size)
                        # print(get_trig(x - player.pos()[0],y -  player.pos()[1]))
                        # print(get_trig(player))
                        enemies.append(
                            player.accelerate(get_trig(player), clicks // 30))
                    Sphere.scale = scale
        if clicks > 0:
            clicks -= 1
        # print(clicks)
        if not self.paused:
            if player.size < 1:
                return game_over(self)
            pygame.draw.circle(self.screen, (0, 30, 255), player.pos(), player.scaled_size())
            player.update()
            # print(player.speed_x,player.speed_y)
            for enemy in enemies.copy():
                pygame.draw.circle(self.screen, enemy.color, enemy.pos(), enemy.scaled_size())
                if not enemy.update():
                    enemies.remove(enemy)
            for enemy in enemies + [player]:
                for enemy2 in enemies + [player]:
                    if enemy2 != enemy:
                        if collision(enemy, enemy2):
                            attack(enemy, enemy2)
            pygame.draw.circle(self.screen, (150, 150, 150),
                               [pos + (player.scaled_size() * 1.5) * dir for pos, dir in
                                zip(player.pos(), get_trig(player))], 5)
            # self.screen.blit(pointer,[pos + (player.scaled_size() * 1.5) * dir for pos, dir in
            #                     zip(player.pos(), get_trig(player))])
            if all([player.size>enemy.size for enemy in enemies]) and not won:
                won=true
                self.paused=true
        else:
            if won:
                if not pause_menu(self,won=true):
                    return false
            else:
                if not pause_menu(self):
                    return false

        pygame.display.update()
        self.clock.tick(self.fps)
