import pygame as pg

class Player:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image_orig = pg.image.load("default.png")
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect(center=screen_rect.center)

    def update(self):
        x,y = pg.mouse.get_pos()
        self.image = pg.transform.scale(self.image_orig, (x,y))
        self.rect = self.image.get_rect(center=self.screen_rect.center)

    def draw(self, surf):
        surf.blit(self.image, self.rect)

screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
done = False
player = Player(screen_rect)
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill((0,0,0))
    player.update()
    player.draw(screen)
    pg.display.update()

