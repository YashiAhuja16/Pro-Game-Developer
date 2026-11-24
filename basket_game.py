
import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("background.png")

class Basket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("basket image.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

b1 = Basket(300, 150)

basket_group = pygame.sprite.Group()
basket_group.add(b1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                b1.rect.x = b1.rect.x - 25

            if event.key == pygame.K_d:
                b1.rect.x = b1.rect.x + 25

            if event.key == pygame.K_LEFT:
                b1.rect.x = b1.rect.x - 25

            if event.key == pygame.K_RIGHT:
                b1.rect.x = b1.rect.x + 25

    screen.blit(bg, (0,0))

    basket_group.draw(screen)

    pygame.display.update()

pygame.quit()
