import pygame
from pygame.locals import *
from scripts.model.text_graph import Interaction
from scripts.utils.window import Window
from scripts.view.character import Player, Npc

class Interaction_view(Window):
    def __init__(self, window :Window, screen :pygame.Surface) -> None:
        self.player = window.map.player
        self.npc = window.closest
        self.npc.interaction.start()
        self.choice = -1
        self.step = False
        self.progress = True
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 32)
        self.display = pygame.Surface((screen.get_width()//16, screen.get_height()//16))
        
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
    
    def on_loop(self) -> str:
        if self.step and self.progress:
            self.step = False
            if not self.npc.interaction.next(self.choice):
                return "village"
        return "interaction"
    
    def on_render(self):
        self.display.fill((150,150,150))
        self.display.blit(self.player.anim.img(), (0, self.display.get_height() - self.player.anim.img().get_height()))
        self.display.blit(self.npc.anim.img(), (
            self.display.get_width()-self.npc.anim.img().get_width(), 
            self.display.get_height() - self.player.anim.img().get_height())
        )
        
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
        lines = self.npc.interaction.get()
        for i in range(0, len(lines)):
            if i:
                text_surf = self.font.render(f"{i}. {lines[i]}", True, (0,0,0))
            else:
                text_surf = self.font.render(lines[i], True, (0,0,0))
            self.screen.blit(text_surf, (
                (self.screen.get_width() - text_surf.get_width())//2,
                self.screen.get_height() - text_surf.get_height()*len(lines) + i * text_surf.get_height()
        ))    