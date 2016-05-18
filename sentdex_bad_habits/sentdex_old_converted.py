import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay_rect = gameDisplay.get_rect()
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

class Car:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        width = 100
        height = 100
        self.set_start()
        self.starty = -100
        self.speed = 7
        self.image = pygame.Surface((width,height)).convert()
        self.image.fill((0,0,0))
        self.set_rect()

    def set_rect(self):
        self.rect = self.image.get_rect(center=(self.startx,self.starty))

    def set_start(self):
        self.startx = random.randrange(0, self.screen_rect.width)

    def reset(self):
        self.set_start()
        self.set_rect()

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_rect.bottom:
            self.reset()
        #if thing_starty > display_height:
        #    thing_starty = 0 - thing_height
        #    thing_startx = random.randrange(0,display_width)

    def draw(self,surface):
        surface.blit(self.image, self.rect)

class Player:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        car_width = 55
        #carImg = pygame.image.load('Car.png') #-->no image to use
        self.image = pygame.Surface((car_width,50)).convert()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(screen_rect.centerx, screen_rect.centery+200))
        self.speed = 5

    def check_collision(self, car_rect):
        if self.rect.colliderect(car_rect):
            return True #switch pause state

    def update(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        self.rect.clamp_ip(self.screen_rect) #keep player in screen

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        #def car(x,y):
        #    gameDisplay.blit(carImg, (x,y))

#-->no need for this, Car.image is the rectange, and Car.draw draws it to the screen
#def thing(thingx, thingy, thingw, thingh, color):
#    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#-->having this split into two functions is redundant, moved to message_display()
#def text_objects(text, font):
#    textSurface = font.render(text, True, black)
#    return textSurface, textSurface.get_rect()


def message_display(text, screen_rect):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    textSurface = largeText.render(text, True, black)
    TextRect = textSurface.get_rect()
    #TextRect.center = ((display_width/2), (display_height/2)) #-->no need for math when you use pygame rects
    TextRect.center = screen_rect.center
    return textSurface, TextRect
    #gameDisplay.blit(TextSurf, TextRect) #-->no need to blit here
    #pygame.display.update() #-->you should only ever see one of these in your entire game
    #time.sleep(2) #-->NEVER use time.sleep in a GUI program
    #game_loop() #-->gameloop only runs once and is ever called once. ACtually you dont even need the content in a function at all

def game_loop():
    gameExit = False
    player = Player(gameDisplay_rect)
    car = Car(gameDisplay_rect)
    msg, msg_rect = message_display('You Crashed!', gameDisplay_rect)
    pause = False
    pause_timer = 0.0
    pause_delay = 3000

    while not gameExit:
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                #-->this is already called at the end of the script, should always use the variable to break
                #pygame.quit()
                #quit()
        if not pause:
            car.update()
            car.draw(gameDisplay)
            player.update(keys)
            player.draw(gameDisplay)
        else:
            gameDisplay.blit(msg, msg_rect)

        #pause if collision
        if player.check_collision(car.rect):
            pause = True

        #reset pause
        if now-pause_timer > pause_delay:
            pause_timer = now
            if pause:
                pause = False
                car.reset()

        pygame.display.update()
        clock.tick(60)


        #-->its better to use pygame.key.get_pressed() for constant key press, located in Player.update()
        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_a:
        #        x_change += -5
        #    if event.key == pygame.K_d:
        #        x_change += 5
        #if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_a or event.key == pygame.K_d:
        #        x_change = 0
        #x += x_change

        #-->This is all handled by Player.check_collision()
        #thingx, thingy, thingw, thingh, color
        #thing(thing_startx, thing_starty, thing_width, thing_height, black)
        #thing_starty += thing_speed
        #car(x,y)
        #if x > display_width - car_width or x < 0:
        #    crash()
        #if y < thing_starty + thing_height:
        #    print('y crossover')
        #    if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
        #        print('x crossover')
        #        crash()

game_loop()
pygame.quit()
quit()
