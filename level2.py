from interactions import *
from game_properties import Properties
from entities import Sphere, Player, Repulsor
from constants import *
from menu import pause_menu, game_over
from level import Level

class Level2(Level):

    def __init__(self, game: Properties):
        super().__init__(game)

    def level_init(self):
        # self.player = Player(20, random.randint(20, game_width - 20), random.randint(20, game_height - 20))
        self.player = Player(30, 400, 400)
        self.player.game=self.game


        self.enemies = [
            Sphere(random.randint(2, 20), random.randint(20, game_width - 20), random.randint(20, game_height - 20)) for
            x in
            range(100)]
        # self.enemies.append(Sphere(150, 700,400))
        self.repulsor=Repulsor(30,800,800)
        for enemy in self.enemies+[self.repulsor]:
            enemy.speed(random.randint(-1, 1) / 1, random.randint(-1, 1) / 1)

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
            # ratio = (width / game_width) * self.scale
            # self.screen.blit(pygame.transform.scale(background, (game_width, game_height)), (round(-player.x*(width/game_width)*scale), round(-player.y*(width/game_width))*scale))
            self.game.screen.blit(
                pygame.transform.scale(background, (round(game_width * self.scale), round(game_height * self.scale))),
                (round(-(self.player.x * self.scale - self.player.pos()[0])),
                 round(-(self.player.y * self.scale - self.player.pos()[1]))))

            if not self.user_interaction_handler():
                return

            if self.clicks > 0:
                self.clicks -= 1
            # print(clicks)
            if not self.paused:
                if self.player.size < 1:
                    return game_over(self.game)

                pygame.draw.circle(self.game.screen, (0, 255, 255), self.player.pos(), self.player.scaled_size())
                self.player.update()
                # print(player.speed_x,player.speed_y)
                for enemy in self.enemies.copy()+[self.repulsor]:
                    if enemy==self.repulsor and self.repulsor.size > 1:
                        pygame.draw.circle(self.game.screen, (255, 255, 255), enemy.pos(), enemy.scaled_size())
                        enemy.update()
                    elif enemy!=self.repulsor:
                        pygame.draw.circle(self.game.screen, enemy.color, enemy.pos(), enemy.scaled_size())
                        if not enemy.update():
                            self.enemies.remove(enemy)
                for enemy in self.enemies + [self.player,self.repulsor]:
                    for enemy2 in self.enemies + [self.player,self.repulsor]:
                        if enemy2 != enemy:
                            if enemy == self.repulsor and enemy.size<enemy2.size:
                                enemy.evade(get_trig_general(enemy, enemy2), distance(enemy, enemy2))
                            if collision(enemy, enemy2):
                                attack(enemy, enemy2)
                pygame.draw.circle(self.game.screen, (150, 150, 150),
                                   [pos + (self.player.scaled_size() * 1.5) * dir for pos, dir in
                                    zip(self.player.pos(), get_trig(self.player))], 5)
                # self.screen.blit(pointer,[pos + (player.scaled_size() * 1.5) * dir for pos, dir in
                #                     zip(player.pos(), get_trig(player))])
                if self.player.size>self.repulsor.size and self.repulsor.size<1 and not self.won:
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
