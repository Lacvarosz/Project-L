import pygame
from scripts.model.map import Map
from scripts.utils.position import Position
from scripts.view.player_view import Player_view
from scripts.utils.load_image import load_image
from scripts.model.tile import Tile
from scripts.view.tiles import Tiles

class Map_view():
    def __init__(self, assets :dict, map :Map, player :Player_view) -> None:
        self.map = map
        self.surf = load_image(map.picture)
        self.player = player
        self.tiles = Tiles(
                [
                    Tile("tree", 1, Position(32, 28), (3,4), (1, 3, 1, 1)),
                    Tile("house", 1, Position(20, 33), (5, 7), (1, 2, 5, 5)),
                ],
                assets,
                16
        )
        
    def update(self, movement :list[int,int] = [0,0]) -> None:
        self.player.update(movement, self.tiles)
    
    def render(self, surf :pygame.Surface) -> None:
        surf.blit(self.surf, (0,0))
        self.tiles.render(surf)
        self.player.render(surf)
    
    def get_size(self) -> tuple[int, int]:
        return(self.surf.get_size())
