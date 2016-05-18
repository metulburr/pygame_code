import pygame as pg

class Block:
    size = 32
    def __init__(self, color, topleft_):
        self.color_init = color
        self.color = color
        self.image = pg.Surface([Block.size, Block.size]).convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=topleft_)

    def update(self):
        self.image.fill(self.color)

    def render(self, screen):
        screen.blit(self.image, self.rect)

class Player:
    def __init__(self, color, topleft_, mapping):
        self.color_init = color
        self.color = color
        self.image = pg.Surface([Block.size, Block.size]).convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=topleft_)

        self.timer = 0.0
        self.new_rect = self.rect.copy()
        self.mapping = mapping

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT: self.set_new_pos('left')
            if event.key == pg.K_RIGHT: self.set_new_pos('right')
            if event.key == pg.K_DOWN: self.set_new_pos('down')
            if event.key == pg.K_UP: self.set_new_pos('up')

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.image.fill(self.color)
        self.animate()

    def animate(self):
        if pg.time.get_ticks()-self.timer > 5:
            self.timer = pg.time.get_ticks()
            if self.rect != self.new_rect:
                if self.marker == 'right':
                    self.rect.x += 1
                elif self.marker == 'down':
                    self.rect.y += 1
                elif self.marker == 'left':
                    self.rect.x -= 1
                elif self.marker == 'up':
                    self.rect.y -= 1
            else:
                self.marker = None

    def set_new_pos(self, direction):
        if not self.marker:
            old = self.new_rect.copy()
            self.marker = direction
            if self.marker == 'right':
                self.new_rect.x += Block.size + 1
            elif self.marker == 'down':
                self.new_rect.y += Block.size + 1
            elif self.marker == 'left':
                self.new_rect.x -= Block.size + 1
            elif self.marker == 'up':
                self.new_rect.y -= Block.size + 1

            if self.out_of_bounds():
                self.new_rect = old

    def out_of_bounds(self):
        if self.new_rect.x > (Block.size*self.mapping.number_of_blocks_wide) or self.new_rect.x < 0:
            return True
        if self.new_rect.y > (Block.size*self.mapping.number_of_blocks_high) or self.new_rect.y < 0:
            return True


class Map:
    def __init__(self):
        self.number_of_blocks_wide = 14
        self.number_of_blocks_high = 14
        self.buffer_width = 1
        self.block_color = (255,255,255)
        self.bg_color = (0,0,0)
        self.block_offsetY = Block.size + self.buffer_width
        self.block_offsetX = Block.size + self.buffer_width
        self.totalsize = (self.number_of_blocks_wide*self.block_offsetX, self.number_of_blocks_high*self.block_offsetY)

    def create_table(self):
        self.board_bg_offset = 1
        self.board_bg = pg.Surface([self.number_of_blocks_wide,self.number_of_blocks_high])
        self.board_bg.fill(self.bg_color)
        self.table = []
        for i in range(self.number_of_blocks_wide):
            row = []
            for j in range(self.number_of_blocks_high):
                row.append(Block(self.block_color, (i*self.block_offsetX, j*self.block_offsetY)))
            self.table.append(row)

    def update(self):
        for row in self.table:
            for block in row:
                block.color = block.color_init

    def render(self, screen):
        screen.blit(self.board_bg, (self.board_bg_offset, self.board_bg_offset))
        for row in self.table:
            for block in row:
                block.render(screen)

class Control:
    def __init__(self):
        self.mapping = Map()
        self.screen = pg.display.set_mode(self.mapping.totalsize)
        self.player = Player((255,0,0), (0,0), self.mapping)
        self.mapping.create_table()
        self.done = False
        self.clock = pg.time.Clock()

    def update(self):
        self.player.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.player.get_event(event)

    def render(self):
        self.mapping.render(self.screen)
        self.player.render(self.screen)
        pg.display.update()

    def mainloop(self):
        while not self.done:
            self.update()
            self.events()
            self.render()
            self.clock.tick(60)

app = Control()
app.mainloop()
