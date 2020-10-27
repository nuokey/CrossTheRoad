import pygame

class Car():
    

size = (1200, 720)

screen = pygame.display.set_mode(size)
pygame.init()
clock = pygame.time.Clock()
done = False
while not done:
    clock.tick(60)
    screen.fill
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()