from pygame import Surface, Rect
from scripts.utils.blitable import Blitable
from concurrent.futures import ThreadPoolExecutor
from scripts.view.tile import Tile

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
        self.closest = None
    
    def _sort_tile_list(self, tiles :list[Blitable]) -> list[Blitable]:
        n = len(tiles)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if tiles[j].has_collision and not tiles[j+1].has_collision:
                    tiles[j], tiles[j+1] = tiles[j+1], tiles[j]
                    swapped = True
                elif tiles[j].get_collision(self.tile_size).bottom > tiles[j+1].get_collision(self.tile_size).bottom:
                    tiles[j], tiles[j+1] = tiles[j+1], tiles[j]
                    swapped = True
            if (swapped == False):
                break
        self.entities = tiles
        return(tiles)
    
    def update(self) -> None:
        pool = ThreadPoolExecutor()
        for e in self.entities:
            pool.submit(e.update)
        pool.shutdown()
        self._sort_tile_list(self.entities)
        if self.npcs:
            self.closest = self.npcs[0]
            for npc in self.npcs:
                if self.player.distance(npc, self.tile_size) < self.player.distance(self.closest, self.tile_size):
                    self.closest = npc        
    
    def render(self, surf :Surface, monitor_rect :Rect) -> None:
        for entity in self.entities:
            # if entity.get_outer_rect(self.tile_size).colliderect(monitor_rect):
            alpha = 255
            if type(entity) == Tile and entity.get_outer_rect(self.tile_size).colliderect(self.player.get_outer_rect(self.tile_size)) and entity.get_collision(self.tile_size).y > self.player.get_outer_rect(self.tile_size).y:
                alpha = 100
            entity.render(surf, self.tile_size, alpha)