import pygame
import time 

pygame.init()
WIDTH = 600
HEIGHT = 600 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("background.png")
class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y 
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

r1 = Rocket(300,300)
rocket_group = pygame.sprite.Group()
rocket_group.add(r1)


while r1.rect.y < 700:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w:
                r1.rect.y = r1.rect.y - 25
            if event.key == pygame.K_a:
                r1.rect.x = r1.rect.x - 25
            if event.key == pygame.K_d:
                r1.rect.x = r1.rect.x + 25
            if event.key == pygame.K_s:
                r1.rect.y = r1.rect.y + 25
    
    screen.blit(bg,(0,0))
    rocket_group.draw(screen)
    
    r1.rect.y += 1 #gravity
    
    pygame.display.update()
screen.fill("red")

font = pygame.font.SysFont("Ariel", 40)
text = font.render("Game Over!", True, "blue")
screen.blit(text, (220,300))
pygame.display.update()
time.sleep(5)
