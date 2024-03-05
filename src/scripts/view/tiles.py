from scripts.model.tile import Tile
from pygame import Surface, Rect
from scripts.utils.position import Position
from scripts.utils.animation import Animation

class Tiles():
    def __init__(self, tiles :list[Tile], assets :dict[str, Animation], tile_size) -> None:
        self.assets = assets
        self.tiles :dict[Tile, Animation]
        self.tiles = {}
        for t in tiles:
            self.tiles[t] = assets[t.type + str(t.variant)].copy()
        self.tile_size = tile_size
    
    def __iter__(self):
        return(iter(self.tiles))
    
    def __getitem__(self, key):
        return(self.tiles[key])
    
    
    def render(self, surf :Surface, monitor_rect :Rect) -> None:
        for tile in self.tiles:
            self.tiles[tile].update()
            if monitor_rect.colliderect(tile.get_outer_rect(self.tile_size)):
                surf.blit(self.tiles[tile].img(), (tile.pos.x*self.tile_size, tile.pos.y*self.tile_size))