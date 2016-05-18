
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()

circle = pygame.Surface([500,300]).convert()
circle.fill((255,0,255)) #make abnormal bg color
circle.set_colorkey((255,0,255)) #hide bg
circle_rect = pygame.draw.circle(circle, (200,200,0), screen_rect.center, 25, 0)

running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(circle, (0,0))
    pygame.display.update()
