from scripts.utils.position import Position
from scripts.utils.load_image import load_images
from scripts.utils.animation import Animation
from scripts.utils.blitable import Blitable
from pygame import Rect

class Tile(Blitable):
    def __init__(self, type_t :str, variant :int, anim: Animation, pos: Position, size: tuple[int, int] = (1,1), collision :tuple[int,int,int,int] = (0,0,1,1)):
        super().__init__(anim, pos)
        self.type = type_t
        self.variant = variant
        self.size = size
        self.collision = collision
    
    def get_collision(self, tile_size: int) -> Rect:
        return (Rect(
                (self.pos.x + self.collision[0]) * tile_size,
                (self.pos.y + self.collision[1]) * tile_size,
                self.collision[2] * tile_size,
                self.collision[3] * tile_size
            ))
    
    def get_outer_rect(self, tile_size :int) -> Rect:
        return(Rect(
                self.pos.x*tile_size,
                self.pos.y*tile_size,
                self.size[0]*tile_size,
                self.size[1]*tile_size
            ))