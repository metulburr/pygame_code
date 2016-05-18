import pygame as pg

pg.init()

text_list = '''I'm Henry the eighth, I am
Henry the eighth, I am, I am
I got married to the widow next door
She's been married seven times before

And every one was an Henry (Henry)
She wouldn't have a Willy or a Sam (No Sam)
I'm her eighth old man, I'm Henry
Henry the eighth I am

Second verse, same as the first

I'm Henry the eighth, I am
Henry the eighth, I am, I am
I got married to the widow next door
She's been married seven times before

And every one was an Henry (Henry)
She wouldn't have a Willy or a Sam (No Sam)
I'm her eighth old man, I'm Henry
Henry the eighth I am

I'm Henry the eighth, I am
Henry the eighth, I am, I am
I got married to the widow next door
She's been married seven times before

And every one was an Henry (Henry)
She wouldn't have a Willy or a Sam (No Sam)
I'm her eighth old man, I'm Henry
Henry the eighth I am

H-E-N-R-Y
Henry (Henry)
Henry (Henry)
Henry the eighth I am, I am
Henry the eighth I am
Yeah!
'''.split('\n')

class Credits:
    def __init__(self, screen_rect, lst):
        self.srect = screen_rect
        self.lst = lst
        self.size = 16
        self.color = (255,0,0)
        self.buff_centery = self.srect.height/2 + 5
        self.buff_lines = 50
        self.timer = 0.0
        self.delay = 50
        self.make_surfaces()


    def make_text(self,message):
        font = pg.font.SysFont('Arial', self.size)
        text = font.render(message,True,self.color)
        rect = text.get_rect(center = (self.srect.centerx, self.srect.centery + self.buff_centery) )
        return text,rect

    def make_surfaces(self):
        self.text = []
        for i, line in enumerate(self.lst):
            l = self.make_text(line)
            l[1].y += i*self.buff_lines
            self.text.append(l)

    def update(self):
        if pg.time.get_ticks()-self.timer > self.delay:
            self.timer = pg.time.get_ticks()
            for text, rect in self.text:
                rect.y -= 1

    def render(self, surf):
        for text, rect in self.text:
            surf.blit(text, rect)

screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
done = False
cred = Credits(screen_rect, text_list)

while not done:
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            done = True
    screen.fill((0,0,0))
    cred.update()
    cred.render(screen)
    pg.display.update()
    clock.tick(60)
