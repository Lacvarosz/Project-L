import pygame
import pygame.locals

class Button():
    def __init__(self, size:tuple[int, int], color:tuple[int,int,int], mouse_over_color:tuple[int,int,int] = None, text:str="Button", text_size:int=12, text_color:tuple[int,int,int]=(0,0,0), text_font:str="Arial", command=lambda : None) -> None:
        self.size = size
        self.text = text
        self.color = color
        self.normal_color = color
        if mouse_over_color is None:
            mouse_over_color = (
                max(color[0]+100, 255),
                max(color[1] + 100, 255),
                max(color[2] + 100, 255)
            )
        self.mouse_over_color = mouse_over_color
        self.text_size = text_size
        self.text_color = text_color
        self.text_font = text_font
        self.command = command
        
        self.surface = pygame.Surface(size, pygame.HWSURFACE)
        self.surface.fill(color)
        self.text = pygame.font.SysFont(text_font, text_size).render(text, True, text_color)
        
        self.has_change = True
    
    def on_event(self, event :pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            if self.color != self.mouse_over_color:
                self.color = self.mouse_over_color
                self.has_change = True
            pos=event.pos 
            print ("x = {}, y = {}".format(pos[0], pos[1]))
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.command()
    
    def on_loop(self) -> None:
        if self.color != self.normal_color:
            self.color = self.normal_color
            self.has_change = True
    
    def update(self) -> None:
        if self.has_change:
            self.text = pygame.font.SysFont(self.text_font, self.text_size).render(self.text, True, self.text_color)
    
    def render(self) -> pygame.Surface:
        if self.has_change:
            self.surface.fill(self.color)
            self.surface.blit(self.text, ((self.size[0] - self.text.get_size()[0])//2, (self.size[1] - self.text.get_size()[1])//2))
            self.has_change = False
        return(self.surface)