import pygame
from pygame.locals import *
from scripts.caracter import Player
from scripts.utils.position import Position
from scripts.utils.load_image import load_image

class Player_view():
    def __init__(self, player :Player) -> None:
        self.player = player
        self.surf = load_image(player.picture)
    
    def update(self, movement :list[int,int]) -> None:
        self.player.move(movement)
    
    def render(self, surf :pygame.Surface) -> None:
        surf.blit(self.surf, self.player.pos.tuple())