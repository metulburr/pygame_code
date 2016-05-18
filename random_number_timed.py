import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
done = False

class Number:
    def __init__(self):
        self.timer = 0.0
        self.delay = 3000
        self.new_num()

    def new_num(self):
        num = random.randint(1,100)
        self.image, self.rect = self.make_text(str(num), (255,0,0), screen_rect.center, 75, 'Ariel')

    def make_text(self,message,color,center,size, fonttype):
        font = pg.font.SysFont(fonttype, size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect

    def update(self):
        if pg.time.get_ticks()-self.timer > self.delay:
            self.timer = pg.time.get_ticks()
            self.new_num()

    def draw(self, surf):
        surf.blit(self.image, self.rect)

num = Number()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill((0,0,0))
    num.update()
    num.draw(screen)
    pg.display.update()
    clock.tick(60)

