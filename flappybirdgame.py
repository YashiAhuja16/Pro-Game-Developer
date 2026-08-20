import pgzrun 
from random import randint


WIDTH = 800
HEIGHT = 600

gravity = 2000.0

class Ball():

    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200 
        self.vy = 0 
        self.radius = 40
    
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.circle(pos,self.radius, "white")

    
    def update(dt):
        uy = ball.vy 
        ball.vy += gravity*dt
        ball.y += (uy+ball.vy) *0.5*dt 
    

    
ball_1 = Ball(50,100)

def draw():
    screen.clear()
    ball_1.draw()








pgzrun.go()

    
