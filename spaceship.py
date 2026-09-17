import pygame 
from pygame.locals import *
from time import *
pygame.init()


WIDTH = 600
HEIGHT = 600 
x_pos = 230
y_pos = 0
keys = [False, False, False, False]

background_image = pygame.image.load("image1.png")
spaceship = pygame.image.load("spaceshipimage.png")


screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.blit(background_image,(0,0))
pygame.display.update()


running = True
while y_pos < 600: 
    screen.blit(spaceship, (x_pos,y_pos))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                y_pos = y_pos - 10
            if event.key == K_LEFT:
                x_pos = x_pos - 10
            if event.key == K_RIGHT:
                x_pos = x_pos + 10
            if event.key == K_DOWN:
                y_pos = y_pos + 10

    y_pos = y_pos + 1
    sleep(0.05)
    screen.blit(background_image,(0,0))
print("GAME OVER!")



pygame.quit()

