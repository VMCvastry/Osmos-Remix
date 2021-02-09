import pygame, random, math, colour

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
true = True
false = False
width = 1200
height = 800
background = pygame.image.load('./assets/background.jpg')
pointer = pygame.image.load('./assets/pointer.png')

game_width = 3600
game_height = 2400

gradient = list(colour.Color('#027afe').range_to(colour.Color('#ff0000'), 102))
print(len(gradient))


# icon=
# playerSize = 10


class Sphere:
    playerSize = 0
    player = None
    scale = 1

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
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.size >= game_width or self.x - self.size <= 0:
            self.speed_x *= -1
        if self.y + self.size >= game_height or self.y - self.size <= 0:
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
        return (width / 2, height / 2)

    def accelerate(self, trig, power):
        x, y = trig
        # if power >=3:
        #     print(str(power)*100)
        if x > 1: x = 1
        if y > 1: y = 1
        if x < -1: x = -1
        if y < -1: y = -1
        new_sphere = Sphere(
            size=math.sqrt(self.size) / (3 / power),
            x=self.x + 1.1 * self.size * x,
            y=self.y + 1.1 * self.size * y
        )
        self.size -= math.sqrt(new_sphere.size) / 1
        increase_x = (new_sphere.size / self.size) * power * x
        increase_y = (new_sphere.size / self.size) * power * y
        self.speed_x -= increase_x
        self.speed_y -= increase_y
        new_sphere.speed(1 / self.size * 100 * x, 1 / self.size * 100 * y)
        return new_sphere


def distance(p1, p2):
    distance = math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
    return distance


def collision(p1, p2) -> bool:
    dis = distance(p1, p2)
    if dis < p1.size + p2.size:
        return true
    else:
        return false


def eat(big: Sphere, small: Sphere):
    reduction = big.size + small.size - distance(big, small)
    ratio = (small.size / big.size) ** 2
    big.size += reduction * ratio
    small.size -= reduction * (1 - ratio)
    big.speed_x += ((small.size / big.size) / 100) * small.speed_x
    big.speed_y += ((small.size / big.size) / 100) * small.speed_y


def attack(p1, p2):
    if p1.size > p2.size:
        eat(p1, p2)
    elif p1.size < p2.size:
        eat(p2, p1)


def set_text(string, coordx, coordy, fontSize):  # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)


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


class GameCore:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Osmos remix')
        self.clock = pygame.time.Clock()
        self.fps = 1000
        # pygame.display.set_icon(icon)
        # self.running = true

    def level_init(self):
        self.paused = false
        self.player = Player(50, random.randint(0, game_width), random.randint(0, game_height))
        self.enemies = [Sphere(random.randint(2, 20), random.randint(0, game_width), random.randint(0, game_height)) for
                        x in
                        range(100)]
        # for enemy in self.enemies:
        #     enemy.speed(random.randint(-1, 1) / 1, random.randint(-1, 1) / 1)

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

    def pause_menu(self):
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

    def level(self):
        self.level_init()
        running = true
        player = self.player
        enemies = self.enemies
        clicks = 0
        scale = 1
        while running:
            self.screen.fill((0, 0, 255))
            # self.screen.blit(background, (0, 0))
            ratio = (width / game_width) * scale
            # self.screen.blit(pygame.transform.scale(background, (game_width, game_height)), (round(-player.x*(width/game_width)*scale), round(-player.y*(width/game_width))*scale))
            self.screen.blit(
                pygame.transform.scale(background, (round(game_width * scale), round(game_height * scale))),
                (round(-(player.x * scale - player.pos()[0])), round(-(player.y * scale - player.pos()[1]))))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return false
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = true
                if not self.paused:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4:
                            if width / player.scaled_size() > 15:
                                scale += 0.1
                        if event.button == 5:
                            if scale > 0.1 and width / player.scaled_size() < 40:
                                scale -= 0.1
                        if event.button == 1:
                            clicks += 50
                            # x, y = pygame.mouse.get_pos()
                            # # print((x-player.x)/player.size,(y-player.y)/player.size)
                            # print(get_trig(x - player.pos()[0],y -  player.pos()[1]))
                            print(get_trig(player))
                            enemies.append(
                                player.accelerate(get_trig(player), clicks // 30))
                        Sphere.scale = scale
            if clicks > 0:
                clicks -= 1
            # print(clicks)
            if not self.paused:
                if player.size < 1:
                    return self.game_over()
                pygame.draw.circle(self.screen, (0, 30, 255), player.pos(), player.scaled_size())
                player.update()
                # Sphere.playerSize = player.size
                for enemy in enemies.copy():
                    pygame.draw.circle(self.screen, enemy.color, enemy.pos(), enemy.scaled_size())
                    if not enemy.update():
                        enemies.remove(enemy)
                for enemy in enemies + [player]:
                    for enemy2 in enemies + [player]:
                        if enemy2 != enemy:
                            if collision(enemy, enemy2):
                                attack(enemy, enemy2)
                pygame.draw.circle(self.screen, (150, 150, 150),
                                   [pos + (player.scaled_size() * 1.5) * dir for pos, dir in
                                    zip(player.pos(), get_trig(player))], 5)
                # self.screen.blit(pointer,[pos + (player.scaled_size() * 1.5) * dir for pos, dir in
                #                     zip(player.pos(), get_trig(player))])
            else:
                if not self.pause_menu():
                    return false

            pygame.display.update()
            self.clock.tick(self.fps)

    def main(self):
        while true:
            retry = self.level()
            if not retry:
                break


if __name__ == '__main__':
    GameCore().main()
