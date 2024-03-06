from scripts.model.tile import Tile
from pygame import Surface, Rect
from scripts.utils.position import Position
from scripts.utils.animation import Animation

class Tiles():
    def __init__(self, tiles :list[Tile], assets :dict[str, Animation], tile_size) -> None:
        self.assets = assets
        self.tiles :dict[Tile, Animation]
        self.tiles = {}
        self.tile_size = tile_size
        for t in self._sort_tile_list(tiles):
            self.tiles[t] = assets[t.type + str(t.variant)].copy()
    
    def __iter__(self):
        return(iter(self.tiles))
    
    def __getitem__(self, key):
        return(self.tiles[key])
    
    def _sort_tile_list(self, tiles :list[Tile]) -> list[Tile]:
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
    
    
    def render(self, surf :Surface, monitor_rect :Rect, player) -> None:
        isnt_blit = True
        for tile in self.tiles:
            self.tiles[tile].update()
            if isnt_blit and tile.get_collision(self.tile_size).bottom > player.player.get_collision().bottom:
                player.render(surf)
                isnt_blit = False
            if monitor_rect.colliderect(tile.get_outer_rect(self.tile_size)):
                surf.blit(self.tiles[tile].img(), (tile.pos.x*self.tile_size, tile.pos.y*self.tile_size))
        if isnt_blit:
            player.render(surf)