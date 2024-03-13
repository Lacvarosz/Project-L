import pygame
from scripts.model.map import Map
from scripts.utils.position import Position
from scripts.view.caracter import Caracter
from scripts.utils.load_image import load_image
from scripts.view.tile import Tile
from scripts.view.entities import Entities
from scripts.utils.animation import Animation

class Map_view():
    def __init__(self, assets :dict[str, Animation], map :Map, player :Caracter) -> None:
        self.map = map
        self.surf = load_image(map.picture)
        self.player = player
        self.tiles = [
                    Tile("tree", 0, assets["tree0"].copy(), Position(32, 28), (3,4), (1, 3, 1, 1)),
                    Tile("house", 0, assets["house0"].copy(), Position(20, 33), (7, 7), (1, 2, 5, 5)),
                    Tile("water", 0, assets["water0"].copy(), Position(11, 11)),
                    Tile("water", 0, assets["water0"].copy(), Position(11, 12)),
                    Tile("water", 0, assets["water0"].copy(), Position(11, 13)),
                    Tile("water", 0, assets["water0"].copy(), Position(11, 14)),
                    Tile("water", 0, assets["water0"].copy(), Position(12, 11)),
                    Tile("water", 0, assets["water0"].copy(), Position(13, 11)),
                    Tile("water", 0, assets["water0"].copy(), Position(12, 12)),
                    Tile("water", 0, assets["water0"].copy(), Position(13, 13)),
                ]
        self.entities = Entities(player, [], self.tiles, 16)
        
    def update(self, movement :list[int,int] = [0,0]) -> None:
        self.player.pre_set(movement, self.entities)
        self.entities.update()
    
    def render(self, surf :pygame.Surface, monitor_rect :pygame.Rect) -> None:
        surf.blit(self.surf, (0,0))
        self.entities.render(surf, monitor_rect)
    
    def get_size(self) -> tuple[int, int]:
        return(self.surf.get_size())
