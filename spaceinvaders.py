import pygame 
WIDTH = 900
HEIGHT = 500
x_pos = 60
y_pos = 200
x_pos1 = 800
y_pos1 = 200


screen = pygame.display.set_mode ((WIDTH, HEIGHT))
background_image = pygame.image.load("background_image.png") 
sprite_1 = pygame.image.load("Image_1.png")
sprite_2 = pygame.image.load("Image.png")

BORDER = pygame.Rect(WIDTH//2 - 5, 0,10,HEIGHT)

sprite_11 = pygame.transform.rotate(pygame.transform.scale(sprite_1,(55,40)), 90)
sprite_22 = pygame.transform.rotate(pygame.transform.scale(sprite_2,(55,40)), 270)

red_bullets = []
yellow_bullets = []

red = pygame.Rect(700,300,55,40)
yellow = pygame.Rect(100,300,55,40)



def draw_window(): 
    screen.blit(background_image, (0,0))
    pygame.draw.rect(screen, (0,0,0), BORDER)
    screen.blit(sprite_11, (x_pos,y_pos))
    screen.blit(sprite_22,(x_pos1, y_pos1))
    for bullet in yellow_bullets: 
        pygame.draw.rect(screen, (255,255,0),bullet)

    
    pygame.display.update()
    
def handle_bullet(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x = bullet.x + 7

    


running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                x_pos = x_pos - 10
            if event.key == pygame.K_d:
                x_pos = x_pos + 10 
            if event.key == pygame.K_s:
                y_pos = y_pos + 10
            if event.key == pygame.K_w: 
                y_pos = y_pos - 10 
            
            if event.key == pygame.K_LEFT:
                x_pos1 = x_pos1 - 10
            if event.key == pygame.K_RIGHT:
                x_pos1 = x_pos1 + 10
            if event.key == pygame.K_UP:
                y_pos1= y_pos1 - 10
            if event.key == pygame.K_DOWN:
                y_pos1 = y_pos1 + 10
            
            if event.key == pygame.K_z:
                bullet = pygame.Rect(yellow.x+ yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                yellow_bullets.append(bullet)
                
        handle_bullet(yellow_bullets, red_bullets, yellow, red)
        draw_window()


pygame.quit()