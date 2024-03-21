from pygame import Surface, HWSURFACE, transform
from scripts.utils.position import Position

class Minimap():    
    def render(self, surf: Surface) -> None:
        surf.blit(transform.scale(surf, (64, 64)), (8, 8))