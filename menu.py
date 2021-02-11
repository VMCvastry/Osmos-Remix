import pygame, random, math, colour
from constants import *

def set_text(string, coordx, coordy, fontSize):  # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)

def game_over(self):
    running = true
    btn1 = pygame.Rect(((width - 200) // 2, 300, 200, 80))
    btn2 = pygame.Rect(((width - 200) // 2, 500, 200, 80))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return false
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        return true
                    if btn2.collidepoint((x, y)):
                        return false
        text0 = set_text("Game Over", width // 2, 70, 50)
        text1 = set_text("Retry", width // 2, 335, 20)
        text2 = set_text("Exit", width // 2, 535, 20)
        pygame.draw.rect(self.screen, (0, 255, 0), btn1)
        pygame.draw.rect(self.screen, (0, 255, 0), btn2)
        self.screen.blit(text0[0], text0[1])
        self.screen.blit(text1[0], text1[1])
        self.screen.blit(text2[0], text2[1])
        pygame.display.update()
        self.clock.tick(self.fps)


def pause_menu(self,won=false):
    running = true
    btn1 = pygame.Rect(((width - 200) // 2, 300, 200, 80))
    btn2 = pygame.Rect(((width - 200) // 2, 500, 200, 80))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return false
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if btn1.collidepoint((x, y)):
                        self.paused = false
                        return true
                    if btn2.collidepoint((x, y)):
                        return false
        if won:
            text0 = set_text("You Won", width // 2, 70, 50)
            text1 = set_text("Continue anyway", width // 2, 335, 20)
        else:
            text0 = set_text("Pause", width // 2, 70, 50)
            text1 = set_text("Resume", width // 2, 335, 20)
        text2 = set_text("Exit", width // 2, 535, 20)
        pygame.draw.rect(self.screen, (0, 255, 0), btn1)
        pygame.draw.rect(self.screen, (0, 255, 0), btn2)
        self.screen.blit(text0[0], text0[1])
        self.screen.blit(text1[0], text1[1])
        self.screen.blit(text2[0], text2[1])

        pygame.display.update()
        self.clock.tick(self.fps)
