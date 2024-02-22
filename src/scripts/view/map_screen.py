import pygame
from scripts.map import Map
from scripts.utils.position import Position
from scripts.view.player_view import Player_view

class Map_view():
    def __init__(self, map :Map, player :Player_view) -> None:
        self.map = map
        self.surf = pygame.image.load(map.picture)
        self.player = player
        self.pos = Position()
        
    def update_surf(self) -> None:
        self.surf = pygame.image.load(self.map.picture)
    
    def calculate_pos(self, size:tuple[int,int]) -> None:
        self.pos = (Position(size[0]/2, size[1]/2) - self.player.player_pos())
    
    def frame(self, size:tuple[int,int], surf :pygame.Surface) -> None:
        self.update_surf()
        self.player.frame(self.surf)
        self.calculate_pos(size)
        surf.blit(self.surf, self.pos.tuple())
    
    def player_moving(self, keys :dict) -> None:
        self.player.moving(keys)
