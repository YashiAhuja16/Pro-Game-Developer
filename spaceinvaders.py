import pygame 
pygame.font.init()
WIDTH = 900
HEIGHT = 500
x_pos = 60
y_pos = 200
x_pos1 = 800
y_pos1 = 200
red_health = 10
yellow_health = 10

RED_HIT = pygame.USEREVENT + 2 
YELLOW_HIT = pygame.USEREVENT + 1


screen = pygame.display.set_mode ((WIDTH, HEIGHT))
background_image = pygame.image.load("background_image.png") 
sprite_1 = pygame.image.load("Image_1.png")
sprite_2 = pygame.image.load("Image.png")

BORDER = pygame.Rect(WIDTH//2 - 5, 0,10,HEIGHT)

sprite_11 = pygame.transform.rotate(pygame.transform.scale(sprite_1,(55,40)), 90)
sprite_22 = pygame.transform.rotate(pygame.transform.scale(sprite_2,(55,40)), 270)

red_bullets = []
yellow_bullets = []


health_font = pygame.font.SysFont('comicsans', 40)

def draw_winner(text):
      draw.text = health_font.render()







def draw_window(red, yellow, red_bullets, yellow_bullets): 
    screen.blit(background_image, (0,0))
    pygame.draw.rect(screen, (0,0,0), BORDER)
    red_health_text = health_font.render("Health: " +str(red_health), 1, (255,255,255))
    screen.blit(red_health_text, (650,10))
    yellow_health_text = health_font.render("Health: "  +str(yellow_health) , 1, (255,255,255))
    screen.blit(yellow_health_text, (10,10))
    screen.blit(sprite_11, (yellow.x,yellow.y))
    screen.blit(sprite_22,(red.x, red.y))
    for bullet in yellow_bullets: 
        pygame.draw.rect(screen, (255,255,0),bullet)
    for bullet1 in red_bullets:
          pygame.draw.rect(screen, (255,0,0), bullet1)
    
    pygame.display.update()
    
def yellow_hw(keypress, yellow):
        if keypress [pygame.K_a]: 
                yellow.x = yellow.x - 10
        if keypress [pygame.K_d]:
                yellow.x = yellow.x + 10 
        if keypress [pygame.K_s]:
                yellow.y = yellow.y + 10
        if keypress [pygame.K_w]: 
                yellow.y = yellow.y - 10 
def red_hw(keypress,red):
        if keypress [pygame.K_LEFT]:
                red.x = red.x - 10
        if keypress [pygame.K_RIGHT]:
                red.x = red.x + 10
        if keypress [pygame.K_UP]:
                red.y= red.y - 10
        if keypress [pygame.K_DOWN]:
                red.y = red.y + 10
     



def handle_bullet(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
            bullet.x = bullet.x + 7
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow_bullets.remove(bullet)
    for bullet in red_bullets:
            bullet.x = bullet.x - 7
            if yellow.colliderect(bullet):
              pygame.event.post(pygame.event.Event(YELLOW_HIT))
              red_bullets.remove(bullet)
    

red = pygame.Rect(700,300,55,40)
yellow = pygame.Rect(100,300,55,40)

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
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
            if event.key == pygame.K_SPACE:
                bullet1 = pygame. Rect(red.x+red.width, red.y+ red.height// 2-2, 10, 5)
                red_bullets.append(bullet1)
        if event.type == RED_HIT:
              red_health = red_health - 1
        if event.type == YELLOW_HIT:
              yellow_health - yellow_health - 1
       
       
        
        keypress = pygame.key.get_pressed()
        red_hw(keypress, red)
        yellow_hw(keypress, yellow)
        handle_bullet(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets)
        


pygame.quit()