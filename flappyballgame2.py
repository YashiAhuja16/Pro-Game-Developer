import pgzrun 
from random import randint


WIDTH = 800
HEIGHT = 600

gravity = 2000.0

class Ball():

    def __init__(self,initial_x,initial_y, vx,vy):
        self.x = initial_x
        self.y = initial_y
        self.vx = vx 
        self.vy = vy
        self.radius = 40
        self.color = (randint(0,255),randint(0,255),randint(0,255))

    
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos,self.radius, self.color) 

    def update(self,dt):
        uy = self.vy 
        self.vy += gravity*dt
        self.y += (uy+self.vy) *0.5*dt 
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius 
            self.vy = - self.vy * 0.9 
            self.x += self.vx*dt
        if self.x > WIDTH - self.radius or self.x < self.radius: 
            self.vx = - self.vx 




    

ball_1 = Ball(50,100,150,0)
ball_2 = Ball(100,150,250,-200)
ball_3 = Ball(150,200,350,-100)
ball_4 = Ball(200,250,-200,-300)
ball_5 = Ball(250,300,-300,100)

def draw():
    screen.clear()
    ball_1.draw()
    ball_2.draw()
    ball_3.draw()
    ball_4.draw()
    ball_5.draw()
def update(dt): 
    ball_1.update(dt) 
    ball_2.update(dt)
    ball_3.update(dt)
    ball_4.update(dt)
    ball_5.update(dt)



pgzrun.go()
