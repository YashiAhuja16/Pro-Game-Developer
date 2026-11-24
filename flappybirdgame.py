import pygame
import time 

pygame.init()
WIDTH = 864
HEIGHT = 768

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("bg.png")

floor = pygame.image.load("floor.png")
floor_x = 0 
game = True 
floor = pygame.transform.scale(floor, (1800, 200))

key_press = False

sprite1 = pygame.image.load("sprite1.png")
sprite2 = pygame.image.load("sprite2.png")
sprite3 = pygame.image.load("sprite3.png")

images = [sprite1, sprite2, sprite3]

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y 
        self.frames = images
        self.index = 0 
        self.counter = 0 
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
    def update(self): 
        self.counter = self.counter + 1
        if self.counter > 10: 
            self.counter = 0
            self.index = self.index + 1 
            if self.index > 2: 
                self.index = 0 

        self.image = self.frames[self.index]




f1 = Bird(75,300)
bird_group = pygame.sprite.Group()
bird_group.add(f1)


while f1.rect.y < 700:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN and key_press == False: 
            if event.key == pygame.K_w:
                f1.rect.y = f1.rect.y - 45
                key_press = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: 
                key_press = False
        
    
    screen.blit(bg,(0,0))
    screen.blit(floor, (floor_x,650))
    bird_group.draw(screen)
    if game == True:
        floor_x = floor_x - 0.6
        if floor_x < -1000:
            floor_x = 0
        bird_group.update()

    f1.rect.y += 1 #gravity

    
    pygame.display.update()
screen.blit(bg,(0,0))
screen.blit(floor, (floor_x,650))
bird_group.draw(screen)

font = pygame.font.SysFont("Ariel", 40)
text = font.render("Game Over!", True, "blue")
screen.blit(text, (220,300))
pygame.display.update()
time.sleep(5)
