import pygame, random, math, colour
from entities import *
from constants import *


def distance(p1, p2):
    dist = math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
    return dist


def collision(p1, p2) -> bool:
    dis = distance(p1, p2)
    if dis < p1.size + p2.size:
        return true
    else:
        return false
def small_reduction_formula(r,R,d):
    return (2*r-d+pow(2*(r**2+R**2)-d**2,0.5))/2
    # return 0.5*(d-2*R+pow(-d**2+4*d*(r+R)-2*(r**2+4*r*R+R**2),0.5))

def eat(big: Sphere, small: Sphere):
    reduction = big.size + small.size - distance(big, small)
    # ratio = (small.size / big.size) ** 4
    # big.size += reduction * ratio
    # small.size -= reduction * (1 - ratio)
    small_reduction=small_reduction_formula(small.size,big.size,distance(big, small))
    small.size-=small_reduction
    big.size+=small_reduction-reduction
    big.speed_x += ((small.size / big.size) / 100) * small.speed_x
    big.speed_y += ((small.size / big.size) / 100) * small.speed_y


def attack(p1, p2):
    if p1.size > p2.size:
        eat(p1, p2)
    elif p1.size < p2.size:
        eat(p2, p1)


def get_trig(player):
    x, y = pygame.mouse.get_pos()
    x, y = [x - player.pos()[0], y - player.pos()[1]]
    # print('x', 'y', x, y)
    hyp = math.sqrt(pow(x, 2) + pow(y, 2))
    sin = y / hyp
    cos = x / hyp
    # print(sin,'sin')
    # print(cos,'cos')
    return cos, sin
