import pygame
from pygame.locals import *
from screeninfo import get_monitors
from scripts.utils.position import Position
from scripts.caracter import Player
from scripts.view.map_screen import Map_view
from scripts.view.player_view import Player_view
from scripts.map import Map

for m in get_monitors():
    if m.is_primary:
        SCREENSIZE = (m.width, m.height)
        break

class App():
    def __init__(self, screensize :tuple[int,int] = SCREENSIZE):
        self.running = False
        self.screensize = screensize
        self.screen = None
        self.map = Map_view(Map(),Player_view(Player(Position(screensize[0]/2, screensize[1]/2),"Chad")))
    
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screensize, RESIZABLE|FULLSCREEN)
        pygame.display.set_caption("Mi na")
        self.running = True
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
    
    def on_loop(self):
        pass
    
    def on_render(self):
        self.screen.fill((0,0,0))
        self.map.frame(self.screensize, self.screen)
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
        self.map.player_moving(pygame.key.get_pressed())
        
    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()