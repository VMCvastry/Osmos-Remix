from constants import *
from game_properties import Properties
from text import set_text


def general_interactions_handler(game: Properties, event):
    """
        handler for general pygame events like video resize and quitting
        Parameters
        ----------
        game : Properties
           game properties to be changed with new size and level values
        event :
           Pygame event
   """
    if event.type == pygame.QUIT:
        game.level = -1
        return false  # game closes
    elif event.type == pygame.VIDEORESIZE:
        new_size = event.dict['size']
        # global width, height
        print(new_size)
        game.width, game.height = new_size
        if game.width < 1200:
            game.width = 1200
        if game.height < 800:
            game.height = 800
        game.screen = pygame.display.set_mode((game.width, game.height),
                                              pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)
    return true


def game_over(game: Properties):
    """
        just game over menu
    """
    while true:
        btn1 = pygame.Rect(((game.width - 200) // 2, 300, 200, 80))
        btn2 = pygame.Rect(((game.width - 200) // 2, 500, 200, 80))
        for event in pygame.event.get():
            if not general_interactions_handler(game, event):
                return false
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        return
                    if btn2.collidepoint((x, y)):
                        game.level = 0
                        return
        text0 = set_text("Game Over", game.width // 2, 70, 50)
        text1 = set_text("Retry", game.width // 2, 335, 20)
        text2 = set_text("Exit", game.width // 2, 535, 20)
        pygame.draw.rect(game.screen, (0, 255, 0), btn1)
        pygame.draw.rect(game.screen, (0, 255, 0), btn2)
        game.screen.blit(text0[0], text0[1])
        game.screen.blit(text1[0], text1[1])
        game.screen.blit(text2[0], text2[1])
        pygame.display.update()
        game.clock.tick(game.fps)


def pause_menu(game: Properties, won=false):
    """
            pause menu, triggered also when user wins
    """
    while true:
        btn1 = pygame.Rect(((game.width - 200) // 2, 300, 200, 80))
        btn2 = pygame.Rect(((game.width - 200) // 2, 500, 200, 80))
        for event in pygame.event.get():
            if not general_interactions_handler(game, event):
                return false
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        return true
                    if btn2.collidepoint((x, y)):
                        game.level = 0
                        return
        if won:
            text0 = set_text("You Won", game.width // 2, 70, 50)
            text1 = set_text("Continue anyway", game.width // 2, 335, 20)
        else:
            text0 = set_text("Pause", game.width // 2, 70, 50)
            text1 = set_text("Resume", game.width // 2, 335, 20)
        text2 = set_text("Exit", game.width // 2, 535, 20)
        pygame.draw.rect(game.screen, (0, 255, 0), btn1)
        pygame.draw.rect(game.screen, (0, 255, 0), btn2)
        game.screen.blit(text0[0], text0[1])
        game.screen.blit(text1[0], text1[1])
        game.screen.blit(text2[0], text2[1])
        pygame.display.update()
        game.clock.tick(game.fps)


def main_menu(game: Properties):
    """
                main menu with level selector
    """
    while true:
        btn1 = pygame.Rect(((game.width - 200) // 2, 300, 200, 80))
        btn2 = pygame.Rect(((game.width - 200) // 2, 500, 200, 80))
        btn3 = pygame.Rect(((game.width - 200) // 2, 700, 200, 80))
        game.screen.fill((0, 0, 255))
        game.screen.blit(menu_background,(0,0))
        for event in pygame.event.get():
            if not general_interactions_handler(game, event):
                return false
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        game.level = 1
                        return
                    if btn2.collidepoint((x, y)):
                        game.level = 2
                        return
                    if btn3.collidepoint((x, y)):
                        game.level = -1
                        return

        text0 = set_text("OSMOS REMIX", game.width // 2, 70, 50)
        text1 = set_text("Level 1", game.width // 2, 335, 20)
        text2 = set_text("Level 2", game.width // 2, 535, 20)
        text3 = set_text("Exit", game.width // 2, 735, 20)
        pygame.draw.rect(game.screen, (0, 255, 0), btn1)
        pygame.draw.rect(game.screen, (0, 255, 0), btn2)
        pygame.draw.rect(game.screen, (0, 255, 0), btn3)
        game.screen.blit(text0[0], text0[1])
        game.screen.blit(text1[0], text1[1])
        game.screen.blit(text2[0], text2[1])
        game.screen.blit(text3[0], text3[1])
        pygame.display.update()
        game.clock.tick(game.fps)
