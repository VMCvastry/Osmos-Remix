import pygame, random, math, colour
from constants import *
from structures import Properties


def set_text(string, coordx, coordy, fontSize):  # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)

def game_over(game: Properties):
    running = true
    btn1 = pygame.Rect(((width - 200) // 2, 300, 200, 80))
    btn2 = pygame.Rect(((width - 200) // 2, 500, 200, 80))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.level = -1
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        return
                    if btn2.collidepoint((x, y)):
                        game.level=0
                        return
        text0 = set_text("Game Over", width // 2, 70, 50)
        text1 = set_text("Retry", width // 2, 335, 20)
        text2 = set_text("Exit", width // 2, 535, 20)
        pygame.draw.rect(game.screen, (0, 255, 0), btn1)
        pygame.draw.rect(game.screen, (0, 255, 0), btn2)
        game.screen.blit(text0[0], text0[1])
        game.screen.blit(text1[0], text1[1])
        game.screen.blit(text2[0], text2[1])
        pygame.display.update()
        game.clock.tick(game.fps)


def pause_menu(game: Properties,won=false):
    running = true
    btn1 = pygame.Rect(((width - 200) // 2, 300, 200, 80))
    btn2 = pygame.Rect(((width - 200) // 2, 500, 200, 80))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.level = -1
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        return true
                    if btn2.collidepoint((x, y)):
                        game.level = 0
                        return
        if won:
            text0 = set_text("You Won", width // 2, 70, 50)
            text1 = set_text("Continue anyway", width // 2, 335, 20)
        else:
            text0 = set_text("Pause", width // 2, 70, 50)
            text1 = set_text("Resume", width // 2, 335, 20)
        text2 = set_text("Exit", width // 2, 535, 20)
        pygame.draw.rect(game.screen, (0, 255, 0), btn1)
        pygame.draw.rect(game.screen, (0, 255, 0), btn2)
        game.screen.blit(text0[0], text0[1])
        game.screen.blit(text1[0], text1[1])
        game.screen.blit(text2[0], text2[1])

        pygame.display.update()
        game.clock.tick(game.fps)

def main_menu(game: Properties):
    game.screen.fill((0, 0, 255))
    running = true
    btn1 = pygame.Rect(((width - 200) // 2, 300, 200, 80))
    btn2 = pygame.Rect(((width - 200) // 2, 500, 200, 80))
    btn3 = pygame.Rect(((width - 200) // 2, 700, 200, 80))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.level = -1
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        game.level=1
                        return
                    if btn2.collidepoint((x, y)):
                        game.level = 2
                        return
                    if btn3.collidepoint((x, y)):
                        game.level = -1
                        return

        text0 = set_text("OSMOS REMIX", width // 2, 70, 50)
        text1 = set_text("Level 1", width // 2, 335, 20)
        text2 = set_text("Level 2", width // 2, 535, 20)
        text3 = set_text("Exit", width // 2, 735, 20)
        pygame.draw.rect(game.screen, (0, 255, 0), btn1)
        pygame.draw.rect(game.screen, (0, 255, 0), btn2)
        pygame.draw.rect(game.screen, (0, 255, 0), btn3)
        game.screen.blit(text0[0], text0[1])
        game.screen.blit(text1[0], text1[1])
        game.screen.blit(text2[0], text2[1])
        game.screen.blit(text3[0], text3[1])
        pygame.display.update()
        game.clock.tick(game.fps)