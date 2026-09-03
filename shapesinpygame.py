import pygame 
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
blue = (0,0,255) 
pygame.display.update()

class Circle():
    def __init__(self,color,position, radius, width):
        self.color = color
        self.pos = position
        self.radius = radius
        self.width = width
        self.surface = screen 
    
    def draw(self): 
        self.draw_circle = pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width) 
    
    def grow(self,r): 
        self.radius = self.radius + r 
        self.draw_circle = pygame.draw.circle(self.surface, self.color,self.pos, self.radius, self.width)

circle1 = Circle(blue, (300,300), 25, 1)


running = True 

while running:
    circle1.draw()
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle1.grow(20)
            pygame.display.update()

pygame.quit() 