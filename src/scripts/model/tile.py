from scripts.utils.position import Position
from scripts.utils.load_image import load_images
from pygame import Rect

class Tile():
    def __init__(self, type_t :str, variant :int, pos :Position, size :tuple[int, int] = (16, 16), collision :tuple[int, int, int, int] = (0,0,16,16)) -> None:
        self.type = type_t
        self.variant = variant
        self.pos = pos
        self.size = size
        
        self.collision = Rect((pos.x+collision[0], pos.y+collision[1]),collision[2:])
        self.outer_rect = Rect(pos.tuple(), size)
    
    def get_collision(self) -> Rect:
        return(self.collision)
    
    def get_outher_rect(self) -> Rect:
        return(self.outer_rect)