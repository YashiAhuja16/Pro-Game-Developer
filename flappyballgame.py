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
        screen.draw.filled_circle(pos,self.radius, "white")

    

def update(dt):
    uy = ball_1.vy 
    ball_1.vy += gravity*dt
    ball_1.y += (uy+ball_1.vy) *0.5*dt 
    if ball_1.y > HEIGHT - ball_1.radius:
        ball_1.y = HEIGHT - ball_1.radius 
        ball_1.vy = - ball_1.vy * 0.9 
    ball_1.x += ball_1.vx*dt
    if ball_1.x > WIDTH - ball_1.radius or ball_1.x < ball_1.radius: 
        ball_1.vx = - ball_1.vx 

def on_key_down(key): 
    if key == keys.SPACE: 
        ball_1.vy = -500 


    

ball_1 = Ball(50,100)

def draw():
    screen.clear()
    ball_1.draw()








pgzrun.go()

    
