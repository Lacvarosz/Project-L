import pygame
from pygame.locals import *
from scripts.model.caracter import Player
from scripts.view.tiles import Tiles
from scripts.utils.load_image import load_image

class Player_view():
    def __init__(self, player :Player) -> None:
        self.player = player
        self.surf = load_image(player.picture)
    
    def update(self, movement :list[int,int], tiles :Tiles) -> None:
        self.player.move(movement,(1024, 1024), tiles)
    
    def render(self, surf :pygame.Surface) -> None:
        surf.blit(self.surf, self.player.pos.tuple())