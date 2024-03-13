from pygame import Surface, Rect
from scripts.utils.blitable import Blitable

class Entities():
    def __init__(self, player, njks, tiles, tile_size) -> None:
        self.tile_size = tile_size
        self.entities :list[Blitable]
        self.entities = self._sort_tile_list([player] + njks + tiles)
    
    def _sort_tile_list(self, tiles :list[Blitable]) -> list[Blitable]:
        n = len(tiles)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if tiles[j].get_collision(self.tile_size).y > tiles[j+1].get_collision(self.tile_size).y:
                    tiles[j], tiles[j+1] = tiles[j+1], tiles[j]
                    swapped = True
            if (swapped == False):
                break
        return(tiles)
    
    def update(self) -> None:
        for e in self.entities:
            e.update()
        self.entities = self._sort_tile_list(self.entities)
    
    
    def render(self, surf :Surface, monitor_rect :Rect) -> None:
        for entity in self.entities:
            if entity.get_outer_rect(self.tile_size).colliderect(monitor_rect):
                entity.render(surf, self.tile_size)