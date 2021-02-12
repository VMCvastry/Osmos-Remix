import pygame, random, math, colour
from constants import *

class Sphere:
    playerSize = 0
    player = None
    scale = 1
    time=1

    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.speed_x = 0
        self.speed_y = 0
        self.set_color()

    def set_color(self):
        if self.size > self.playerSize:
            self.color = (255, 0, 255)
        else:
            # print(round(self.size/self.playerSize*100))
            try:
                self.color = [round(x * 255) for x in gradient[round(self.size / self.playerSize * 100)].rgb]
            except Exception as error:
                print(error)
                print(round(self.size / self.playerSize * 100))
                print(self.size / self.playerSize * 100)
                print(self.size)
                print(self.playerSize)
            # print(self.color)

    def update(self):
        if self.size < 1:
            return false
        self.move()
        self.set_color()
        return true

    def move(self) -> None:
        self.x += self.speed_x*self.time
        self.y += self.speed_y*self.time
        if (self.x + self.size >= game_width and self.speed_x>0) or (self.x - self.size <= 0 and self.speed_x<0):
            self.speed_x *= -1
        if (self.y + self.size >= game_height and self.speed_y>0) or (self.y - self.size <= 0 and self.speed_y<0):
            self.speed_y *= -1

    def speed(self, x: float, y: float) -> None:
        self.speed_x += x
        self.speed_y += y

    def pos(self):
        return (self.x - self.player.x) * self.scale + self.player.pos()[0], (self.y - self.player.y) * self.scale + \
               self.player.pos()[1]

    def scaled_size(self):
        return self.size * self.scale


class Player(Sphere):
    def update(self):
        self.move()
        Sphere.playerSize = self.size
        Sphere.player = self

    def pos(self):
        return width / 2, height / 2

    def accelerate(self, trig, power):
        x, y = trig
        # if power >=3:
        #     print(str(power)*100)
        force=self.size*power*10
        new_sphere = Sphere(
            size=pow(force,0.2) ,
            x=self.x + 1.5 * self.size * x,
            y=self.y + 1.5 * self.size * y
        )
        # self.size -= math.sqrt(new_sphere.size) / 1
        if self.size**2-new_sphere.size**2<0:
            self.size=0
            return new_sphere
        self.size=math.sqrt(self.size**2-new_sphere.size**2)
        increase_x = (force/self.size**2) * x
        increase_y = (force/self.size**2) * y
        self.speed_x -= increase_x
        self.speed_y -= increase_y
        new_sphere.speed((force/new_sphere.size**2) * x, (force/new_sphere.size**2) * y)
        return new_sphere

        # new_sphere = Sphere(
        #     size=math.sqrt(self.size) / (3 / power),
        #     x=self.x + 1.1 * self.size * x,
        #     y=self.y + 1.1 * self.size * y
        # )
        # self.size -= math.sqrt(new_sphere.size) / 1
        # increase_x = (new_sphere.size / self.size) * power * x
        # increase_y = (new_sphere.size / self.size) * power * y
        # self.speed_x -= increase_x
        # self.speed_y -= increase_y
        # new_sphere.speed(1 / self.size * 100 * x, 1 / self.size * 100 * y)
        # return new_sphere

class Repulsor(Sphere):
    def evade(self,trig,distance):
        cos ,sin =trig
        self.speed_x-= (10000/distance**2 )*cos
        self.speed_y -= (10000/ distance ** 2) * sin
