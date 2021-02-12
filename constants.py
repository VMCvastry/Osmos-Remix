import pygame, random, math, colour
true = True
false = False
width = 1200
height = 800
game_width = 3600
game_height = 2400
gradient = list(colour.Color('#027afe').range_to(colour.Color('#ff0000'), 102))
background = pygame.image.load('./assets/background2.jpg')
pointer = pygame.image.load('./assets/pointer.png')
# icon=

def set_text(string, coordx, coordy, fontSize):  # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)