from interactions import *
from game_properties import Properties
from entities import Sphere, Player
from constants import *
from menu import pause_menu, game_over
from level import Level


class Level1(Level):
    """
            first level become the biggest
            """

    def __init__(self, game: Properties):
        super().__init__(game)

    def level_init(self):
        self.player = Player(20, random.randint(20, game_width - 20), random.randint(20, game_height - 20))
        self.player.game = self.game
        self.enemies = [
            Sphere(random.randint(2, 40), random.randint(40, game_width - 40), random.randint(40, game_height - 40)) for
            x in
            range(200)]  # spawn random enemies
        for enemy in self.enemies:
            enemy.speed(random.randint(-1, 1), random.randint(-1, 1))  # set random speed to reduce impasse

    def run_level(self):
        while self.running:
            self.game.screen.fill((0, 0, 255))  # background outside level space
            self.game.screen.blit(
                pygame.transform.scale(background, (round(game_width * self.scale), round(game_height * self.scale))),
                (round(-(self.player.x * self.scale - self.player.pos()[0])),
                 round(-(self.player.y * self.scale - self.player.pos()[1]))))  # level space backgorund sync with player position

            if not self.user_interaction_handler():
                return
            if self.clicks > 0:  # very rudimentary way of knowing number of rapid clicks
                self.clicks -= 1
            if not self.paused:
                if self.player.size < 1:
                    return game_over(self.game)
                pygame.draw.circle(self.game.screen, (0, 30, 255), self.player.pos(), self.player.scaled_size())
                self.player.update()
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

                if all([self.player.size > enemy.size for enemy in self.enemies]) and not self.won:  # check if user is the biggest
                    self.won = true
                    self.paused = true
            else:
                if self.won:
                    if not pause_menu(self.game, won=true):
                        return false
                    else:
                        self.paused = false
                else:
                    if not pause_menu(self.game):
                        return false
                    else:
                        self.paused = false

            pygame.display.update()
            self.game.clock.tick(self.game.fps)
