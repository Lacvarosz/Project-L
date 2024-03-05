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
                    Tile("tree", 0, Position(32, 28), (3,4), (1, 3, 1, 1)),
                    Tile("house", 0, Position(20, 33), (7, 7), (1, 2, 5, 5)),
                    Tile("water", 0, Position(11, 11)),
                    Tile("water", 0, Position(11, 12)),
                    Tile("water", 0, Position(11, 13)),
                    Tile("water", 0, Position(11, 14)),
                    Tile("water", 0, Position(12, 11)),
                    Tile("water", 0, Position(13, 11)),
                    Tile("water", 0, Position(12, 12)),
                    Tile("water", 0, Position(13, 13)),
                ],
                assets,
                16
        )
        
    def update(self, movement :list[int,int] = [0,0]) -> None:
        self.player.update(movement, self.tiles)
    
    def render(self, surf :pygame.Surface, monitor_rect :pygame.Rect) -> None:
        surf.blit(self.surf, (0,0))
        self.tiles.render(surf, monitor_rect)
        self.player.render(surf)
    
    def get_size(self) -> tuple[int, int]:
        return(self.surf.get_size())
