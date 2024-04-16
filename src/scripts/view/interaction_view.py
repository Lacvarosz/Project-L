import pygame
from pygame.locals import *
from scripts.model.text_graph import Interaction
from scripts.utils.window import Window
from scripts.view.character import Player, Npc

class Interaction_view(Window):
    def __init__(self, player :Player, npc :Npc, screen :pygame.Surface) -> None:
        self.player = player
        self.npc = npc
        self.npc.interaction.start()
        self.choice = -1
        self.step = False
        self.progress = True
        self.screen = screen
        self.font = pygame.font.Font("src/fonts/Mystic Root Regular.ttf", 15)
        
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
            self.step = False
    
    def on_render(self):
        self.screen.fill((150,150,150))
        self.screen.blit(self.player.anim.img(), (0, self.screen.get_height() - self.player.anim.img().get_height()))
        self.screen.blit(self.npc.anim.img(), (
            self.screen.get_width()-self.npc.anim.img().get_width(), 
            self.screen.get_height() - self.player.anim.img().get_height())
        )
        text_surf = self.font.render("\n\t".join(self.npc.interaction.get()), True, (0,0,0))
        self.screen.blit(text_surf, (
            (self.screen.get_width() - text_surf.get_width())//2,
            self.screen.get_height() - text_surf.get_height()
        ))
    
    