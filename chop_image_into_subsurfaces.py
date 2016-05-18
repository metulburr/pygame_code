import pygame as pg

pg.init()

def strip_from_sheet(sheet, start, size, columns, rows=1):
    """
    Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows.
    """
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames

screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
done = False
sheet = pg.image.load('default.png')
size = sheet.get_size()
frames = strip_from_sheet(sheet, (0,0), (size[0]/2,size[1]), 2,1)


while not done:
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            done = True
    screen.blit(frames[0], (0,0))
    pg.display.update()
