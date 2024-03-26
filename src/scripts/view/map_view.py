import pygame
from scripts.model.map import Map
from scripts.utils.position import Position
from scripts.view.character import Character
from scripts.utils.load_image import load_image
from scripts.view.tile import Tile
from scripts.view.entities import Entities
from scripts.utils.animation import Animation
from scripts.view.character import Npc
from scripts.ml.int_reader import Interact_reader

import os

class Map_view():
    def __init__(self, assets :dict[str, Animation], map :Map, player :Character, tile_size :int) -> None:
        self.map = map
        self.surf = load_image(map.picture)
        self.player = player

        reader = Interact_reader()
        elder_text, elder_file = reader.read(open("src/test/interaction text format.txt", "r"))
        elder_file.close()
        
        self.npcs = [
            Npc(elder_text, assets["village_elder"].copy() ,Position(32,32) * tile_size, True, "Village Elder", 0.2, (1,2),(0,1,1,1)),
        ]
        self.tiles = [
                    Tile("tree", "green", assets["tree_green"].copy(), Position(32, 28), True, (3,4), (1, 3, 1, 1)),
                    Tile("house", "simple", assets["house_simple"].copy(), Position(20, 33), True, (7, 7), (1, 2, 5, 5)),
                    Tile("house", "peasent", assets["house_peasent"], Position(14, 23), True, (6,8), (1,2,4,6)),
                    Tile("house", "villageelder", assets["house_villageelder"], Position(38, 21), True, (8,10), (1,3,6,6)),
                    Tile("water", "light", assets["water_light"].copy(), Position(11, 11)),
                    Tile("water", "light", assets["water_light"].copy(), Position(11, 12)),
                    Tile("water", "light", assets["water_light"].copy(), Position(11, 13)),
                    Tile("water", "light", assets["water_light"].copy(), Position(11, 14)),
                    Tile("water", "light", assets["water_light"].copy(), Position(12, 11)),
                    Tile("water", "light", assets["water_light"].copy(), Position(13, 11)),
                    Tile("water", "light", assets["water_light"].copy(), Position(12, 12)),
                    Tile("water", "light", assets["water_light"].copy(), Position(13, 13)),
                ]
        self.entities = Entities(player, self.npcs, self.tiles, tile_size)
        
    def update(self, movement :list[int,int] = [0,0]) -> None:
        self.player.pre_set(movement)
        self.entities.update()
    
    def render(self, surf :pygame.Surface, monitor_rect :pygame.Rect) -> None:
        surf.blit(self.surf, (0,0))
        self.entities.render(surf, monitor_rect)
    
    def get_size(self) -> tuple[int, int]:
        return(self.surf.get_size())
