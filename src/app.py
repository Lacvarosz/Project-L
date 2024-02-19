import pygame
from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Square, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()

class App():
    def __init__(self) -> None:
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.square1 = Square()
        self.square2 = Square()
        self.square3 = Square()
        self.square4 = Square()
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.blit(self.square1.surf, (40, 40))
        self._display_surf.blit(self.square2.surf, (40, 530))
        self._display_surf.blit(self.square3.surf, (730, 40))
        self._display_surf.blit(self.square4.surf, (730, 530))
        
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
            
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
    