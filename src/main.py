import pygame
from pygame.locals import *
from screeninfo import get_monitors
from scripts.utils.animation import Animation
from scripts.utils.load_image import *
from scripts.view.main_menu import Main_menu
from scripts.view.village import Village
from scripts.utils.window import Window

for m in get_monitors():
    if m.is_primary:
        SCREENSIZE = (m.width, m.height)
        break

class App():
    def __init__(self, screensize :tuple[int,int] = SCREENSIZE):
        self.running = False
        self.screensize = screensize
        self.screen = None
        self.window :Window
        self.state = "main_menu"
    
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screensize, RESIZABLE|FULLSCREEN)
        pygame.display.set_caption("Mi na")
        
        self.assets = {
                "house_simple" : Animation(load_images("house/simple"), 10),
                "house_peasent" : Animation(load_images("house/peasent"), 10),
                "house_villageelder" : Animation(load_images("house/villageelder"), 10),
                "tree_green" : Animation(load_images("tree/green"), 7),
                "water_light": Animation(load_images("water/light"),30),
                "player": Animation([load_image("characters/main character.png")], 1),
                "village_elder": Animation([load_image("characters/village elder.png")],1),
                "button" : load_image("button.png")
            }
        
        self.window = Main_menu(self.assets, self.screensize, self.screen)
        
        
        self.running = True
        self.clock = pygame.time.Clock()
    
    def on_event(self, event :pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
        self.window.on_event(event)
    
    def on_loop(self):
        state = self.window.on_loop()
        if state != self.state:
            self.state = state
            if state == "village":
                self.window = Village(self.screensize, self.assets, self.screen)
            elif state == "main_menu":
                self.window = Main_menu(self.assets, self.screensize, self.screen)
            else:
                self.running = False
                   
    def on_render(self):
        self.screen.fill((50,50,50))
        self.window.on_render()
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
            self.clock.tick()
        self.on_cleanup()
        
    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()