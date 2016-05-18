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
            if num > -.5 and num < .5: #restrict ball direction to avoid infinity bounce
                continue
            else:
                return num
                
    def set_ball(self):
        '''get random starting direction and set ball to center screen'''
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
            print('side wall hit, time to reset ball and give points')
            
    def collide_paddle(self, paddle_rect):
        if self.rect.colliderect(paddle_rect):
            self.vel[0] *= -1;
            
    def move(self):
        self.true_pos[0] += self.vel[0] * self.speed
        self.true_pos[1] += self.vel[1] * self.speed
        self.rect.center = self.true_pos
            
    def update(self, paddle_rect):
        self.collide_walls()
        self.collide_paddle(paddle_rect)
        self.move()

    def render(self, screen):
        screen.blit(self.image, self.rect)
        
class Paddle:
    def __init__(self, screen_rect, size):
        self.screen_rect = screen_rect
        self.image = pg.Surface(size).convert()
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.x += 25 #spacer from wall
        self.speed = 5
        
    def move(self, x, y):
        self.rect[0] += x * self.speed
        self.rect[1] += y * self.speed
        
    def update(self, keys):
        self.rect.clamp_ip(self.screen_rect)
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.move(0, -1)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.move(0, 1)
        
    def render(self, screen):
        screen.blit(self.image, self.rect)

paddle = Paddle(screen_rect, (25,100))
ball = Ball(screen_rect, (25,25))

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    keys = pg.key.get_pressed()
    screen.fill((0,0,0))
    paddle.update(keys)
    ball.update(paddle.rect)
    paddle.render(screen)
    ball.render(screen)
    clock.tick(60)
    pg.display.update()
