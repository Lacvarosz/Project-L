import pygame
from pygame.locals import *
from scripts.utils.animation import Animation
from scripts.model.map import Map
from scripts.utils.load_image import *
from scripts.utils.position import Position
from scripts.view.map_view import Map_view
from scripts.view.character import Player
from scripts.view.minimap import Minimap
from scripts.utils.window import Window

class Village(Window):
    def __init__(self, screensize :tuple[int,int], assets : dict[str, Animation], screen :pygame.Surface):
        self.running = False
        self.screensize = screensize
        self.assets = assets
        self.upscale = 4
        self.tile_size = 16
        self.screen = None
        self.movement = [0,0]
        self.screen = screen
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
        if event.type == KEYUP:
            if event.key in [K_UP, K_w]:
                self.movement[1] += 1
            if event.key in [K_DOWN, K_s]:
                self.movement[1] -= 1
            if event.key in [K_LEFT, K_a]:
                self.movement[0] += 1
            if event.key in [K_RIGHT, K_d]:
                self.movement[0] -= 1
    
    def on_loop(self):
        self.map.update(self.movement)
    
    def on_render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.display, self.map.player.subsurface_rect(self.screensize, self.upscale, self.map.get_size()))
        # print(self.display.get_size())
        self.screen.blit(pygame.transform.scale_by(self.display.subsurface(
                self.map.player.subsurface_rect(self.screensize, self.upscale, self.map.get_size())
            ), self.upscale), (0,0))
        pygame.display.update()