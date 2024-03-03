from scripts.model.text_graph import Interaction, Node
from scripts.utils.position import Position
from scripts.view.tiles import Tiles, Tile
import pygame

class Caracter():
    def __init__(self, pos :Position = Position(), name:str="NJK", speed :int = 5, size = 16, collision = (0,1,1,1)) -> None:
        self.name = name
        self.pos = pos
        self.speed = speed
        self.picture = "onlychar.png"
        self.collision = collision
        self.size = size
    
    def get_collision(self) -> pygame.Rect:
        return(pygame.Rect(self.pos.x + self.collision[0]*self.size, self.pos.y + self.collision[1]*self.size, self.collision[2]*self.size, self.collision[3]*self.size))
        

class Player(Caracter):
    def __init__(self, pos: Position = Position(), name: str = "NJK", speed: int = 1, size=16, collision=(0, 1, 1, 1)) -> None:
        super().__init__(pos, name, speed, size, collision)
    
    def move(self, movement :list[int,int] = [0, 0], map_size: tuple[int, int] = (1024, 1024), tiles :Tiles = Tiles([], [], 0)) -> None:
        self.pos.x += movement[0] * self.speed
        
        p_loc = pygame.Rect((self.pos.x // self.size) + self.collision[0], (self.pos.y // self.size) + self.collision[1], self.collision[2], self.collision[3])
        for tile in tiles:
            if p_loc.colliderect(tile.collision):
                if movement[0] > 0:
                    p_loc.right = tile.collision.left
                if movement[0] < 0:
                    p_loc.left = tile.collision.right
                self.pos.x = (p_loc.x - self.collision[0])*self.size
        
        self.pos.y += movement[1] * self.speed
        
        p_loc = pygame.Rect((self.pos.x // self.size) + self.collision[0], (self.pos.y // self.size) + self.collision[1], self.collision[2], self.collision[3])
        for tile in tiles:
            if p_loc.colliderect(tile.collision):
                if movement[1] > 0:
                    p_loc.bottom = tile.collision.top
                if movement[1] < 0:
                    p_loc.top = tile.collision.bottom
                self.pos.y = (p_loc.y - self.collision[1])*self.size
                    
        # Map edge
        if self.pos.x + self.size > map_size[0]:
            self.pos.x = map_size[0] - self.size
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y + self.size*2 > map_size[1]:
            self.pos.y = map_size[1] - self.size*2
        if self.pos.y < 0:
            self.pos.y = 0
    
    def offset(self, size :tuple[int,int]) -> tuple[int,int]:
        return(
            ((size[0]//2 - self.pos.x), (size[1]//2 - self.pos.y))
        )
        
    def subsurface_rect(self, size :tuple[int,int], upscale : int, map_size :tuple[int, int] = (1024, 1024)) -> pygame.Rect:
        size = (size[0]//upscale, size[1]//upscale)
        left_top = [max(-self.offset(size)[0], 0), max(-self.offset(size)[1], 0)]
        
        if left_top[0] + size[0] > map_size[0]:
            left_top[0] = max(map_size[0] - size[0], 0)
        if left_top[1] + size[1] > map_size[1]:
            left_top[1] = max(map_size[1] - size[1], 0)
        return(pygame.Rect(left_top, size))