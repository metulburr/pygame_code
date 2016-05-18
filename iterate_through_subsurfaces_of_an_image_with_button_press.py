import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()

def strip_from_sheet(sheet, start, size, columns, rows=1):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames

dice_sheet = pg.image.load('dice.png')
dice = strip_from_sheet(dice_sheet, (0,0), (36,36), 1, 6)

class Button:
    def __init__(self, screen_rect):
        self.image = pg.Surface([100,50]).convert()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=screen_rect.center)
    def render(self, surf):
        surf.blit(self.image, self.rect)

image = pg.Surface([0,0]).convert()
btn = Button(screen_rect)
done = False
while not done:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if btn.rect.collidepoint(pg.mouse.get_pos()):
                image = random.choice(dice)
    screen.blit(image, (0,0))
    btn.render(screen)
    pg.display.update()


'''EXPLANATION

    pg.init()
    screen = pg.display.set_mode((800,600))
    screen_rect = screen.get_rect()

Here we are doing pygame.init(), creating the display, and creating a rect for the display for positioning things to the screen. 

    def strip_from_sheet(sheet, start, size, columns, rows=1):
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                frames.append(sheet.subsurface(pg.Rect(location, size)))
        return frames

The strip from sheet function is only used once here, but normally you use it over and over to load numerous spritesheets. The function loops through the spritesheet creating a subsurface for each image and returns a list of the images as pygame surfaces. This function assumes all images are of the same size and organized. You cannot use this function to obtain specific coordinates of a spritesheet. 

    dice_sheet = pg.image.load('dice.png')
    dice = strip_from_sheet(dice_sheet, (0,0), (36,36), 1, 6)

Here we load the spritesheet, and then run the strip from sheet function on it to obtain the individual images. The arguments from left to right... sheet is the spritesheet you want to use, (0,0) is starting on the topleft of the spritesheet, (36,36) is the size of each image, and there is 1 column of images, and 6 images per row. 

    class Button:
        def __init__(self, screen_rect):
            self.image = pg.Surface([100,50]).convert()
            self.image.fill((255,0,0))
            self.rect = self.image.get_rect(center=screen_rect.center)
        def render(self, surf):
            surf.blit(self.image, self.rect)

Here we define the Button class. It takes a screen_rect argument when created in the dunder init method __init__(constructor). it creates an image of the size (100,50) as well as fills the image with color red. The third line in the dunder init creates the objects rect from the image. The rect is of the same size as the image, and the image will be drawn to this position. So if you move the rect, the image moves with it. The argument center position the rect to screen_rect.center. Which basically just assigns the rect center position to (400,300), screen_rect.center value, which is the middle of the screen. The render method gets called in the main game loop to draw the button. It gets passed the screen, and blits the image to the recct position. 

    image = pg.Surface([0,0]).convert()
    btn = Button(screen_rect)
    done = False

here we are creating an image with no size. This basically just satisfy's the fact that you do not want the image to be shown until you press the button. IF you wanted one of the images to be shown you could replace this line with the one in the while loop "image = random.choice(dice)". We create a Button object and send it the screen rect for positioning as well as the done variable for terminating the program. 

     while not done:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

We start the main game loop using the done variable to terminate it. We fill the screen black. We start the event loop and check if the user presses the x button to terminate program, and if so terminate it. 

    elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        if btn.rect.collidepoint(pg.mouse.get_pos()):
            image = random.choice(dice)

Here we check the event for a mouse button down and that it is the left button. We then make a condition to check if the mouse position is inside the rect of the btn object. If so, then it redefines the image that is being drawn to a new one. random.choice(dice) returns a random selection from the dice list to a new image that is being drawn. 

    screen.blit(image, (0,0))
    btn.render(screen)
    pg.display.update()

Lastly, we draw the image (whatever it may be) to the screen at the topleft position (0,0). Before you press the button at all, it is the bogus surface "image = pg.Surface([0,0]).convert()" to just make sure that there is an image. But after that the image is one of the dice subsurfaces. The second line runs the objects render method which draws the button to the screen. And the last one is the pygame display update to update the screen. 
'''

