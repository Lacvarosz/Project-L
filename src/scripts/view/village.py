import pygame
from typing import Self
from pygame.locals import *
from scripts.utils.animation import Animation
from scripts.model.map import Map
from scripts.utils.load_image import *
from scripts.utils.position import Position
from scripts.view.map_view import Map_view
from scripts.view.character import Player
from scripts.utils.window import Window
from scripts.view.minimap import Minimap

class Village(Window):
    _village = None
    
    def __init__(self, assets : dict[str, Animation], screen :pygame.Surface):
        self.running = False
        self.screensize = screen.get_size()
        self.assets = assets
        self.upscale = 4
        self.tile_size = 16
        self.screen = None
        self.movement = [0,0]
        self.interact = False
        self.closest = None
        self.screen = screen
        self.state = "village"
        pygame.display.set_caption("Mi na")
        self.map = Map_view(self.assets, Map(),Player(
            self.assets["player"],
            Position(self.screensize[0]//2//self.upscale, self.screensize[1]//2//self.upscale),
            True,
            "Chad",
            1,
            (1,2),
            (0,1,1,1)
        ), self.tile_size)
        self.display = pygame.Surface(self.map.get_size(),HWSURFACE)
        self.minimap = pygame.Surface((self.map.get_size()[0]//4, self.map.get_size()[1]//4),HWSURFACE)
        
        self.minimap = Minimap
    
    @classmethod
    def village(cls, assets : dict[str, Animation], screen :pygame.Surface) -> Self:
        if cls._village == None:
            cls._village = Village(assets, screen)
        cls._village.state = "village"
        return cls._village

    def on_event(self, event :pygame.event.Event):
        if event.type == KEYDOWN:
            if event.key in [K_UP, K_w]:
                self.movement[1] -= 1
            if event.key in [K_DOWN, K_s]:
                self.movement[1] += 1
            if event.key in [K_LEFT, K_a]:
                self.movement[0] -= 1
            if event.key in [K_RIGHT, K_d]:
                self.movement[0] += 1
            if event.key == K_RETURN:
                self.interact = True
        if event.type == KEYUP:
            if event.key in [K_UP, K_w]:
                self.movement[1] += 1
            if event.key in [K_DOWN, K_s]:
                self.movement[1] -= 1
            if event.key in [K_LEFT, K_a]:
                self.movement[0] += 1
            if event.key in [K_RIGHT, K_d]:
                self.movement[0] -= 1
    
    def on_loop(self) -> str:
        self.map.update(self.movement)
        if self.interact :
            self.closest = self.map.entities.closest
            if self.map.entities.player.pos.distance(self.closest.pos) < 2*self.tile_size and self.closest.interaction is not None:
                self.state = "interaction"
            self.interact = False
        return self.state
    
    def on_render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.display, self.map.player.subsurface_rect((self.screensize[0], self.screensize[1]), self.upscale, self.map.get_size()))
        # print(self.display.get_size())
        seeable = self.display.subsurface(
                self.map.player.subsurface_rect((self.screensize[0], self.screensize[1]), self.upscale, self.map.get_size())
            )
        self.screen.blit(pygame.transform.scale_by(seeable, self.upscale), (0,0))
        self.screen.blit(pygame.transform.scale(self.display, (self.map.get_size()[0]//4, self.map.get_size()[1]//4)), (10, 10))