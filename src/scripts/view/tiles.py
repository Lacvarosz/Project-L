from scripts.model.tile import Tile

class Tiles():
    def __init__(self, tiles :list[Tile], assets) -> None:
        self.tiles = {}
        for t in tiles:
            self.tiles[t] = assets[t.type][t.variant-1]
    
    def __iter__(self):
        return(iter(self.tiles))
    
    def __getitem__(self, key):
        return(self.tiles[key])