import pygame, random, math, colour


def set_text(string, coordx, coordy, fontSize):
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, (168, 50, 152))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)