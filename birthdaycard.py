import pygame, time
pygame.init()


WIDTH = 500
HEIGHT = 500
background_image = pygame.image.load("image_1.jpeg")
background_image2 = pygame.image.load("image_2.jpeg")
background_image2 = pygame.transform.scale(background_image2,(WIDTH,HEIGHT))
font = pygame.font.SysFont("Times New Roman",36)
text = font.render("Happy Birthday.", True, (0,0,255))

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))

running = True
screen.blit(background_image,(0,0))
pygame.display.update()
screen.blit(background_image2,(0,0))
pygame.display.update()
screen.blit(text,(10,10))
pygame.display.update()
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

pygame.quit()
