import pygame
from scripts.model.map import Map
from scripts.utils.position import Position
from scripts.view.player_view import Player_view
from scripts.utils.load_image import load_image
from scripts.model.tile import Tile

class Map_view():
    def __init__(self, assets :dict, map :Map, player :Player_view) -> None:
        self.map = map
        self.surf = load_image(map.picture)
        self.player = player
        self.tiles = [
                Tile(assets, "tree", 1, Position(344, 133), (48,64), (16, 48, 16, 16)),
                Tile(assets, "house", 1, Position(512, 512), (80, 112), (0, 32, 80, 80)),
            ]
        
    def update(self, movement :list[int,int] = [0,0]) -> None:
        self.player.update(movement)
    
    def render(self, surf :pygame.Surface) -> None:
        surf.blit(self.surf, (0,0))
        for t in self.tiles:
            surf.blit(t.surf, t.pos.tuple())
        self.player.render(surf)
    
    def get_size(self) -> tuple[int, int]:
        return(self.surf.get_size())
