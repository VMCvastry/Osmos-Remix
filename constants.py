import pygame, random, math, colour  # import modules here for all files
true = True
false = False
# width = 1200
# height = 800
game_width = 3600
game_height = 2400
gradient = list(colour.Color('#027afe').range_to(colour.Color('#ff0000'), 102))
background = pygame.image.load('./assets/background2.jpg')
menu_background = pygame.image.load('./assets/menuBackground.jpg')
pointer = pygame.image.load('./assets/pointer.png')
icon=pygame.image.load('./assets/icon.png')

