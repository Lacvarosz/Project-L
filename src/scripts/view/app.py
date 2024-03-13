import pygame
from pygame.locals import *
from screeninfo import get_monitors
from scripts.utils.animation import Animation
from scripts.model.map import Map
from scripts.utils.load_image import *
from scripts.utils.position import Position
from scripts.view.map_view import Map_view
from scripts.view.caracter import Caracter

for m in get_monitors():
    if m.is_primary:
        SCREENSIZE = (m.width, m.height)
        break

class App():
    def __init__(self, screensize :tuple[int,int] = SCREENSIZE):
        self.running = False
        self.screensize = screensize
        self.upscale = 4
        self.screen = None
        self.movement = [0,0]
    
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screensize, RESIZABLE|FULLSCREEN)
        pygame.display.set_caption("Mi na")
        
        self.assets = {
                "house0" : Animation(load_images("house/0"), 10),
                "tree0" : Animation(load_images("tree/0"), 7),
                "water0": Animation(load_images("water/0"),30),
                "player": Animation([load_image("onlychar.png")], 1)
            }
        
        self.running = True
        self.clock = pygame.time.Clock()
        self.map = Map_view(self.assets, Map(),Caracter(
            self.assets["player"],
            Position(self.screensize[0]//2//self.upscale, self.screensize[1]//2//self.upscale),
            "Chad",
            1,
            (1,2),
            (0,1,1,1)
        ))
        self.display = pygame.Surface(self.map.get_size(),HWSURFACE)
    
    def on_event(self, event :pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
            if event.key == K_UP:
                self.movement[1] -= 1
            if event.key == K_DOWN:
                self.movement[1] += 1
            if event.key == K_LEFT:
                self.movement[0] -= 1
            if event.key == K_RIGHT:
                self.movement[0] += 1
        if event.type == KEYUP:
            if event.key == K_UP:
                self.movement[1] += 1
            if event.key == K_DOWN:
                self.movement[1] -= 1
            if event.key == K_LEFT:
                self.movement[0] += 1
            if event.key == K_RIGHT:
                self.movement[0] -= 1
    
    def on_loop(self):
        self.map.update(self.movement)
    
    def on_render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.display, self.map.player.subsurface_rect(self.screensize, self.upscale, self.map.get_size()))
        # print(self.display.get_size())
        self.screen.blit(pygame.transform.scale_by(self.display.subsurface(
                self.map.player.subsurface_rect(self.screensize, self.upscale, self.map.get_size())
            ), self.upscale), (0,0))
        pygame.display.update()
    
    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
        
        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            print(self.clock.get_fps(), end="\r")
            self.clock.tick(120)
        self.on_cleanup()
        
    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()