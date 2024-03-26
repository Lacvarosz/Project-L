import pygame
from scripts.utils.position import Position
from scripts.view.map_view import Map_view

class Minimap():
    def __init__(self, pos :Position, screensize :tuple[int,int], upscale :int, map:Map_view) -> None:
        self.pos = pos
        self.size = (screensize[0]//4, screensize[1]//4)
        self.screensize = screensize
        self.map = map
        self.upscale = upscale
    
    def uppdate(self) -> None:
        self.map.player.subsurface_rect((self.screensize[0]//2, self.screensize[1]//2), self.upscale, self.map.get_size())
        
        
    def render(self, surf : pygame.Surface) ->None:
        surf.blit(self.surf, self.pos.tuple())