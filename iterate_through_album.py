import pygame

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
photo = pygame.image.load('default.png').convert_alpha()
photo2 = pygame.image.load('default2.png').convert_alpha()
album = [photo, photo2]
index = 0
timer = 0.0
done = False

while not done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if pygame.time.get_ticks()-timer > 1000:
        timer = pygame.time.get_ticks()
        index += 1
        if index >= len(album):
            index = 0
    image = album[index]
    screen.blit(image, (0,0))
    pygame.display.update()
    clock.tick(60)
