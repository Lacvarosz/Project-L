import pygame
from pygame.locals import *
from scripts.caracter import Player
from scripts.utils.position import Position

class Player_view():
    def __init__(self, player :Player) -> None:
        self.player = player
        self.surf = pygame.transform.scale_by(pygame.image.load(self.player.picture), 0.02)
    
    def player_pos(self) -> Position:
        return(self.player.pos)
    
    def frame(self, surf :pygame.Surface) -> None:
        surf.blit(self.surf, self.player_pos().tuple())
        
    def moving(self, keys :dict) -> None:
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self.player.move_left(3)
        if keys[K_RIGHT] or keys[K_d]:
            self.player.move_right(3)
        if keys[K_UP] or keys[K_w]:
            self.player.move_up(3)
        if keys[K_DOWN] or keys[K_s]:
            self.player.move_down(3)