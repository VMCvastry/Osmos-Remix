from constants import *
from level1 import Level1
from level2 import Level2
from game_properties import Properties
from menu import main_menu


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class GameCore:
    """
       The outermost level class of the game
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Osmos remix')
        self.game = Properties()
        pygame.display.set_icon(icon)

    def main(self):
        """
              just a main menu wrapper, and level selector
        """
        while self.game.level != -1:
            if self.game.level == 1:
                Level1(self.game).run_level()
            elif self.game.level == 2:
                Level2(self.game).run_level()
            elif self.game.level == 0:
                main_menu(self.game)


if __name__ == '__main__':
    GameCore().main()
