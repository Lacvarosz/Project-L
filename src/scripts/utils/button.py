import pygame
import pygame.locals
from scripts.utils.position import Position

class Button():
    def __init__(self, global_position:Position, size:tuple[int, int] = None, color:tuple[int,int,int]=(100,100,100), image :pygame.Surface  = None, text:str="Button", text_size:int=12, text_color:tuple[int,int,int]=(0,0,0), command=lambda : None) -> None:
        self.size = size
        self.text = text
        self.color = color
        self.alpha = 100
        self.text_size = text_size
        self.text_color = text_color
        self.command = command
        self.image = image
        if image is not None:
            self.size = image.get_size()
            self.surface = self.image
        else:
            self.surface = pygame.Surface(self.size, pygame.HWSURFACE)
        
        self.global_position = global_position
        
        self.surface.set_colorkey((0,0,0))
        self.text_surf :pygame.Surface
        
        self.has_change = True
    
    def on_event(self, event :pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            if self.over_button(event.pos):
                if self.alpha != 255:
                    self.alpha = 255
                    self.has_change = True
            elif self.alpha != 100:
                self.alpha = 100
                self.has_change = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.over_button(event.pos):
                self.command()
    
    def on_loop(self) -> None:
            self.update()
    
    def update(self) -> None:
        if self.has_change:
            self.text_surf = pygame.font.Font("src/fonts/Mystic Root Regular.ttf", self.text_size).render(self.text, True, self.text_color)
            self.surface.set_alpha(self.alpha)
    
    def render(self) -> pygame.Surface:
        if self.has_change:
            if self.image is None:
                self.surface.fill(self.color)
            else:
                self.surface.blit(self.image, (0,0))
            self.surface.blit(self.text_surf, ((self.size[0] - self.text_surf.get_size()[0])//2, (self.size[1] - self.text_surf.get_size()[1])//2))
            self.has_change = False
        return(self.surface)
    
    def over_button(self, pos :tuple[int, int]) -> bool:
        return (self.global_position.x <= pos[0] and
                self.global_position.x + self.size[0] >= pos[0] and
                self.global_position.y + self.size[1] >= pos[1] and
                self.global_position.y <= pos[1])