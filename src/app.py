import pygame
from pygame.locals import *
from screeninfo import get_monitors
from utils.position import Position
from caracter import Player
from map import Map

for m in get_monitors():
    if m.is_primary:
        SCREENSIZE = (m.width, m.height)
        break

class App():
    def __init__(self, screensize :tuple[int,int] = SCREENSIZE):
        self.running = False
        self.screensize = screensize
        self.screen = None
        self.player_obj = Player(Position(screensize[0]/2, screensize[1]/2),"Chad")
        self.map_obj = Map(Position(), self.player_obj)
    
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screensize, pygame.RESIZABLE|pygame.FULLSCREEN)
        pygame.display.set_caption("Mi na")
        self.running = True
        self.player = pygame.image.load(self.player_obj.picture)
        self.player = pygame.transform.scale_by(self.player, 0.1)
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
    
    def on_loop(self):
        pass
    
    def on_render(self):
        self.map_obj.set_pos(self.screensize)
        self.map = pygame.image.load(self.map_obj.picture)
        self.map.blit(self.player, (self.player_obj.pos.tuple()))
        self.screen.fill((0,0,0))
        self.screen.blit(self.map, (self.map_obj.pos.tuple()))
        pygame.display.update()
    
    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
        
        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.mooving()
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
    def mooving(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self.player_obj.move_left(5)
        if keys[K_RIGHT] or keys[K_d]:
            self.player_obj.move_right(5)
        if keys[K_UP] or keys[K_w]:
            self.player_obj.move_up(5)
        if keys[K_DOWN] or keys[K_s]:
            self.player_obj.move_down(5)
        
    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()