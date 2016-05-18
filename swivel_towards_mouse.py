##REOURCES
#http://i.imgur.com/CUwMqS9.png


#import pygame
import random
import math

background_colour = (255,255,255)
(width, height) = (800, 600)

BLACK = (0,0,0)
clock = pygame.time.Clock()

def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i, val in enumerate(v) ]

def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i, val in enumerate(v)))

def add(u, v):
    return [ u[i]+v[i] for i, val in enumerate(u) ]

def sub(u, v):
    return [ u[i]-v[i] for i, val in enumerate(u) ]    

class Block(pygame.sprite.Sprite):
    """
   This class represents the ball.
   It derives from the "Sprite" class in Pygame.
   """

    def __init__(self, screenrect):
        """ Constructor. Pass in the color of the block,
       and its x and y position. """

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.masterimage = pygame.image.load("enemy_bullet.png")
        self.image = self.masterimage
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect(center=screenrect.center)
        self.target = self.rect.center
        #self.angle = 0
        self.angle = self.get_angle()
        self.speed = 4
        self.set_target(screenrect.center)

    def get_angle(self):
        mouse = pygame.mouse.get_pos()
        image_facing = 272
        offset = (mouse[1]-self.rect.centery, mouse[0]-self.rect.centerx)
        self.angle = image_facing-math.degrees(math.atan2(*offset))
        self.image = pygame.transform.rotate(self.masterimage, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set_target(self, pos):
        self.target = pos

    def update(self):
        if self.rect.center != self.target:
            target_vector = sub(self.target, self.rect.center) 
            if magnitude(target_vector) > 2: 
                move_vector = [c * self.speed for c in normalize(target_vector)]
                self.rect.x, self.rect.y = add((self.rect.x, self.rect.y), move_vector)

    def render(self, screen):
        screen.blit(self.image, self.rect)

screen = pygame.display.set_mode((width, height))
obj = Block(screen.get_rect())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            obj.get_angle()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            obj.set_target(pygame.mouse.get_pos())

    screen.fill(background_colour)
    obj.update()
    obj.render(screen)
    clock.tick(60)
    pygame.display.flip()
