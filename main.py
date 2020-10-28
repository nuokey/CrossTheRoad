import pygame
from random import randint as rnd

class Player():
    def __init__(self):
        self.x = 600
        self.y = 600
        self.image = pygame.image.load('player.png')
    
    def draw(self):
        global done
        screen.blit(self.image, (self.x, self.y))

        if abs(self.y - car.y) < 150 and abs(self.x - car.x) < 160:
            print('Вы проиграли!!!')
            done = True

        if self.y <= - 200:
            print('Вы выиграли!!!')
            done = True

class Car():
    def __init__(self):
        self.image = pygame.image.load('car.png')
        self.speed = rnd(-1, 1)
        self.x = -200
        if self.speed == 1:
            self.x = 1400
        elif self.speed == -1:
            self.x = -200
        else:
            self.speed = 1

        self.y = rnd(0, 3)
        self.y *= 150

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        self.x += self.speed * 7

        if self.x > 1280 or self.x < -200:
            self.__init__()

size = (1280, 720)
player = Player()
car = Car()

screen = pygame.display.set_mode(size)
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
                player.y -= 20
            if event.key == pygame.K_s:
                player.y += 20

    player.draw()
    car.draw()

    pygame.display.flip()
pygame.quit()