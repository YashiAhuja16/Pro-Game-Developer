import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((0,0,0))

pygame.display.update()

class Rectangle(): 
    
    def __init__(self,color,dimensions):
        self.rect_surface = screen 
        self.rect_color = color
        self.rect_dimensions = dimensions 
    
    def draw(self):
        self.draw_rect = pygame.draw.rect(self.rect_surface, self.rect_color, self.rect_dimensions)




Big_Rectangle = Rectangle()
