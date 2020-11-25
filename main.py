import pygame
from random import randint as rnd

class Player():
    def __init__(self):
        self.x = 600
        self.y = 0
        self.texture = pygame.image.load('player.png')
    
    def draw(self):
        x = self.x
        y = self.y * 150
        texture = pygame.transform.scale(self.texture, (75, 150))
        screen.blit(texture, (x, y))

        for car in cars:
            if abs(self.y - car.y) < 150 and abs(self.x - car.x) < 160:
                pass

            if self.y <= - 200:
                pass

class Car():
    def __init__(self, y):
        self.image = pygame.image.load('car.png')
        self.speed = rnd(-1, 1)
        self.x = -200
        if self.speed == -1:
            self.x = rnd(1400, 2000)
        elif self.speed == 1:
            self.x = rnd(-1000, -200)
        else:
            self.speed = 1

        self.y = y
        self.y *= 150

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        self.x += self.speed * 7

        if self.x > 2000 or self.x < -1000:
            self.__init__(self.y // 150)

size = (1280, 720)
player = Player()
cars = []
for i in range(4):
    cars.append(Car(i))

screen = pygame.display.set_mode(size)
pygame.display.set_caption('CrossTheRoad | by NuoKey')
pygame.init()
clock = pygame.time.Clock()
done = False
while not done:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.y -= 1
            if event.key == pygame.K_s:
                player.y += 1
            if event.key == pygame.K_ESCAPE:
                done = True
    player.draw()
    for i in cars:
        i.draw()

    pygame.display.flip()
pygame.quit()