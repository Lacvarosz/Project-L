import pygame
from pygame.locals import *
from scripts.utils.animation import Animation
from scripts.utils.position import Position
from scripts.view.entities import Entities
from scripts.utils.load_image import load_image
from scripts.utils.blitable import Blitable

from random import randint

class Character(Blitable):
    def __init__(self, anim: Animation, pos: Position, has_collision :bool, name :str, speed :int, size :tuple[int,int], collision :tuple[int,int,int,int]):
        super().__init__(anim, pos, has_collision)
        self.name = name
        self.speed = speed
        self.collision = collision
        self.size = size
        self.movement = [0,0]
        self.entities :Entities
    
    def get_collision(self, tile_size: int) -> pygame.Rect:
        return(pygame.Rect(
            self.pos.x + self.collision[0] * tile_size,
            self.pos.y + self.collision[1] * tile_size,
            self.collision[2] * tile_size,
            self.collision[3] * tile_size
        ) if self.has_collision else self.get_outer_rect(tile_size))
    
    def get_outer_rect(self, tile_size: int) -> pygame.Rect:
        return(pygame.Rect(
            self.pos.x,
            self.pos.y,
            self.size[0] * tile_size,
            self.size[1] * tile_size
        ))
    
    def update(self) -> None:
        self.move(self.entities, self.movement,(1024, 1024))
    
    def set_entities(self, entities: Entities) -> None:
        self.entities = entities
    
    def render(self, surf: pygame.Surface, tile_size: int) -> None:
        surf.blit(self.anim.img(), (self.pos).tuple())
    
    def move(self, entites :Entities, movement :list[int,int] = [0, 0], map_size: tuple[int, int] = (1024, 1024), tile_size :int = 16) -> bool:
        
        ret = True
        self.pos.x += (movement[0] * self.speed)
        
        p_loc = self.get_collision(tile_size)
        for e in entites.entities:
            if e.has_collision:
                t_coll = e.get_collision(tile_size)
                if e is not self and p_loc.colliderect(t_coll):
                    if movement[0] > 0:
                        p_loc.right = t_coll.left
                    if movement[0] < 0:
                        p_loc.left = t_coll.right
                    self.pos.x = p_loc.x - self.collision[0]*tile_size
                    ret = False
        
        self.pos.y += movement[1] * self.speed
        
        p_loc = self.get_collision(tile_size)
        for e in entites.entities:
            if e.has_collision:
                t_coll = e.get_collision(tile_size)
                if e is not self and p_loc.colliderect(t_coll):
                    if movement[1] > 0:
                        p_loc.bottom = t_coll.top
                    if movement[1] < 0:
                        p_loc.top = t_coll.bottom
                    self.pos.y = p_loc.y - self.collision[1]*tile_size
                    ret = False
                    
        # Map edge
        if self.pos.x + self.size[0] * tile_size > map_size[0]:
            self.pos.x = map_size[0] - self.size[0]*tile_size
            ret = False
        if self.pos.x < 0:
            self.pos.x = 0
            ret = False
        if self.pos.y + self.size[1] * tile_size > map_size[1]:
            self.pos.y = map_size[1] - self.size[1]*tile_size
            ret = False
        if self.pos.y < 0:
            self.pos.y = 0
            ret = False
        return ret

class Player(Character):
    def __init__(self, anim: Animation, pos: Position, has_collision: bool, name: str, speed: int, size: tuple[int, int], collision: tuple[int, int, int, int]):
        super().__init__(anim, pos, has_collision, name, speed, size, collision)
    
    def pre_set(self, movement :list[int, int]) -> None:
        self.movement = movement
    
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


class Npc(Character):
    def __init__(self, anim: Animation, pos: Position, has_collision: bool, name: str, speed: int, size: tuple[int, int], collision: tuple[int, int, int, int]):
        super().__init__(anim, pos, has_collision, name, speed, size, collision)
        self.movement = [randint(-1, 1), randint(-1, 1)]
        
    def update(self) -> None:
        if not self.move(self.entities, self.movement, (1024, 1024)):
            self.movement = [randint(-1, 1), randint(-1, 1)]
            while 0 == self.movement[0] and 0 == self.movement[1]:
                self.movement = [randint(-1, 1), randint(-1, 1)]
            self.pos.to_int()