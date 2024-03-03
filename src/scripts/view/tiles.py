from scripts.model.tile import Tile
from pygame import Surface
from scripts.utils.position import Position

class Tiles():
    def __init__(self, tiles :list[Tile], assets :dict, tile_size) -> None:
        self.assets = assets
        self.tiles = tiles
        self.tile_size = tile_size
    
    def __iter__(self):
        return(iter(self.tiles))
    
    def __getitem__(self, key):
        return(self.tiles[key])
    
    def render(self, surf :Surface) -> None:
        for tile in self.tiles:
            surf.blit(self.assets[tile.type][tile.variant-1], (tile.pos.x*self.tile_size, tile.pos.y*self.tile_size))