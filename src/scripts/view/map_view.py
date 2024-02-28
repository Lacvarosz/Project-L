import pygame
from scripts.map import Map
from scripts.utils.position import Position
from scripts.view.player_view import Player_view
from scripts.utils.load_image import load_image

class Map_view():
    def __init__(self, map :Map, player :Player_view) -> None:
        self.map = map
        self.surf = load_image(map.picture)
        self.player = player
        
    def update(self, movement :list[int,int] = [0,0]) -> None:
        self.player.update(movement)
    
    def render(self, surf :pygame.Surface) -> None:
        surf.blit(self.surf, (0,0))
        self.player.render(surf)
    
    def get_size(self) -> tuple[int, int]:
        return(self.surf.get_size())
