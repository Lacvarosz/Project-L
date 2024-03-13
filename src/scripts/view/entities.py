from pygame import Surface, Rect
from scripts.utils.blitable import Blitable
from concurrent.futures import ThreadPoolExecutor

class Entities():
    def __init__(self, player, npcs, tiles, tile_size) -> None:
        self.tile_size = tile_size
        for npc in npcs:
            npc.set_entities(self)
        player.set_entities(self)
        self.npcs = npcs
        self.player = player
        self.tiles = tiles
        self.entities :list[Blitable]
        self.entities = self._sort_tile_list([player] + npcs + tiles)
    
    def _sort_tile_list(self, tiles :list[Blitable]) -> list[Blitable]:
        n = len(tiles)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if tiles[j].has_collision and not tiles[j+1].has_collision:
                    tiles[j], tiles[j+1] = tiles[j+1], tiles[j]
                    swapped = True
                elif tiles[j].get_collision(self.tile_size).y > tiles[j+1].get_collision(self.tile_size).y:
                    tiles[j], tiles[j+1] = tiles[j+1], tiles[j]
                    swapped = True
            if (swapped == False):
                break
        return(tiles)
    
    def update(self) -> None:
        pool = ThreadPoolExecutor()
        for e in self.entities:
            pool.submit(e.update)
        pool.shutdown()
        self.entities = self._sort_tile_list(self.entities)
    
    
    def render(self, surf :Surface, monitor_rect :Rect) -> None:
        for entity in self.entities:
            if entity.get_outer_rect(self.tile_size).colliderect(monitor_rect):
                entity.render(surf, self.tile_size)