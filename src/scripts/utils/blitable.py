from pygame import Rect, Surface
from  typing import Self
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
    
    def distance(self, b :Self, tile_size :int) -> float:
        r1, r2 = self.get_collision(tile_size), b.get_collision(tile_size)
        p1, p2 = Position(), Position()
        if r1.top > r2.top:
            p1.y, p2.y = r1.top, r2.bottom
        else:
            p1.y, p2.y = r1.bottom, r2.top
        if r1.left > r2.left:
            p1.x, p2.x = r1.left, r2.right
        else:
            p1.x, p2.x = r1.right, r2.left
        return p1.distance(p2)
    
    def __str__(self) -> str:
        return(str(self.get_collision(16).y))