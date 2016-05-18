
import pygame as pg
import random

screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
done = False

class Ball:
    def __init__(self, screen_rect, size):
        self.screen_rect = screen_rect
        self.height, self.width = size
        self.image = pg.Surface(size).convert()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.set_ball()

    def get_random_float(self):
        '''get float for velocity of ball on starting direction'''
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -.5 and num < .5:
                continue
            else:
                return num
                
    def set_ball(self):
        x = self.get_random_float()
        y = self.get_random_float()
        self.vel = [x, y]
        self.rect.center = self.screen_rect.center
        self.true_pos = list(self.rect.center)
        
    def collide_walls(self):
        if self.rect.y < 0 or self.rect.y > self.screen_rect.bottom - self.height:
            self.vel[1] *= -1;
            
        if self.rect.x < 0 or self.rect.x > self.screen_rect.right- self.height:
            self.vel[0] *= -1;
            
    def move(self):
        self.true_pos[0] += self.vel[0] * self.speed
        self.true_pos[1] += self.vel[1] * self.speed
        self.rect.center = self.true_pos
            
    def update(self):
        self.collide_walls()
        self.move()

    def render(self, screen):
        screen.blit(self.image, self.rect)

ball = Ball(screen_rect, (50,50))

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill((0,0,0))
    ball.update()
    ball.render(screen)
    clock.tick(60)
    pg.display.update()

