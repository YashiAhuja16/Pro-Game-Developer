import pygame 
WIDTH = 900
HEIGHT = 500
x_pos = 60
y_pos = 200
x_pos1 = 800
y_pos1 = 200


screen = pygame.display.set_mode ((WIDTH, HEIGHT))
background_image = pygame.image.load("background_image.png") 
sprite_1 = pygame.image.load("Image.png")
sprite_2 = pygame.image.load("Image_1.png")

sprite_11 = pygame.transform.rotate(pygame.transform.scale(sprite_1,(55,40)), 90)
sprite_22 = pygame.transform.rotate(pygame.transform.scale(sprite_2,(55,40)), 270)

screen.blit(background_image, (0,0))
screen.blit(sprite_11, (x_pos,y_pos))
screen.blit(sprite_22,(x_pos1, y_pos1))


running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 







pygame.quit()