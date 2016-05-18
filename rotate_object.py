import pygame as pg

screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
done = False

class Rotator:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.master_image = pg.Surface([100,100]).convert_alpha()
        self.master_image.fill((255,0,0))
        self.image = self.master_image.copy()
        self.rect = self.image.get_rect(center=self.screen_rect.center)
        self.delay = 10
        self.timer = 0.0
        self.angle = 0

    def new_angle(self):
        self.angle += 1
        self.angle %= 360

    def rotate(self):
        self.new_angle()
        self.image = pg.transform.rotate(self.master_image, self.angle)
        self.rect = self.image.get_rect(center=self.screen_rect.center)

    def update(self):
        if pg.time.get_ticks()- self.timer > self.delay:
            self.timer = pg.time.get_ticks()
            self.rotate()

    def draw(self, surf):
        surf.blit(self.image, self.rect)

rotator = Rotator(screen_rect)

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill((0,0,0))
    rotator.update()
    rotator.draw(screen)
    pg.display.update()

