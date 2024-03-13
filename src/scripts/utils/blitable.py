from pygame import Rect, Surface
from scripts.utils.position import Position
from scripts.utils.animation import Animation

class Blitable():
    def __init__(self, anim :Animation, pos :Position, has_collision = True):
        self.anim = anim
        self.pos = pos
        self.has_collision = has_collision
        
        
    def get_collision(self, tile_size :int) -> Rect:
        pass
    
    def get_outer_rect(self, tile_size :int) -> Rect:
        pass
    
    def update(self) -> None:
        self.anim.update()
    
    def render(self, surf :Surface, tile_size :int, alpha :int) -> None:
        img = self.anim.img()
        img.set_alpha(alpha)
        surf.blit(img, (self.pos * tile_size).tuple())
    
    def __str__(self) -> str:
        return(str(self.get_collision(16).y))