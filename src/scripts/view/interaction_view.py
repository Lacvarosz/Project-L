import pygame
from pygame.locals import *
from scripts.model.text_graph import Interaction
from scripts.utils.window import Window
from scripts.view.character import Player, Npc

class Interaction_view(Window):
    def __init__(self, player :Player, npc :Npc) -> None:
        self.player = player
        self.npc = npc
        self.npc.interaction.start()
        self.choice = -1
        self.step = False
        self.progress = True
        
    def on_event(self, event :pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_1:
                self.choice = 0
                self.step = True
            if event.key == K_2:
                self.choice = 1
                self.step = True
            if event.key == K_3:
                self.choice = 2
                self.step = True
            if event.key == K_4:
                self.choice = 3
                self.step = True
            if event.key == K_5:
                self.choice = 4
                self.step = True
    
    def on_loop(self):
        if self.step and self.progress:
            self.npc.interaction.next(self.choice)
    
    def on_render(self):
        return super().on_render()