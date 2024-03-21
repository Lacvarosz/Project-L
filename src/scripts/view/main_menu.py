import pygame
from pygame.event import Event
from scripts.utils.window import Window
from scripts.utils.animation import Animation
from scripts.utils.button import Button

class Main_menu(Window):
    def __init__(self, assets :dict[str, Animation], screensize : tuple[int, int], screen :pygame.Surface) -> None:
        self.screensize = screensize
        self.screen = screen
        self.assets = assets
        self.new_game_b = Button((50,20),(100,100,100), text="New Game",command=self.new_game)
        self.state = "main_menu"
    
    def on_event(self, event: Event):
        self.new_game_b.on_event(event)
    
    def on_loop(self) -> str:
        self.new_game_b.on_loop()
        return(self.state)
    
    def on_render(self):
        self.screen.blit(self.new_game_b.render(), (
            (self.screensize[0] - self.new_game_b.size[0]) // 2,
            (self.screensize[1] - self.new_game_b.size[1]) // 2
        ))
    
    def new_game(self):
        self.state = "village"