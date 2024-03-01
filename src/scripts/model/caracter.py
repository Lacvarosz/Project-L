from scripts.model.text_graph import Interaction, Node
from scripts.utils.position import Position
import pygame

class Caracter():
    def __init__(self, pos :Position = Position(), name:str="NJK", speed :int = 5, size = (16,32), collision = (0,16,16,16)) -> None:
        self.name = name
        self.pos = pos
        self.speed = speed
        self.picture = "onlychar.png"
        self.collision = collision
        self.size = size
    
    def get_collision(self) -> pygame.Rect:
        return(pygame.Rect(self.pos.x + self.collision[0], self.pos.y + self.collision[1], self.collision[2], self.collision[3]))
        

class Player(Caracter):
    def __init__(self, pos: Position = Position(), name: str = "NJK", speed :int = 2) -> None:
        super().__init__(pos, name, speed)
    
    def move(self, movement :list[int,int] = [0, 0], map_size: tuple[int, int] = (1024, 1024)) -> None:
        self.pos.x += movement[1] * self.speed
        self.pos.y += movement[0] * self.speed
    
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