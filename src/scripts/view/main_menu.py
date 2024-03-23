import pygame
from pygame.event import Event
from pygame import Surface
from scripts.utils.window import Window
from scripts.utils.animation import Animation
from scripts.utils.button import Button
from scripts.utils.position import Position

class Main_menu(Window):
    def __init__(self, assets :dict[str, Animation], screensize : tuple[int, int], screen :pygame.Surface) -> None:
        self.screensize = screensize
        self.screen = screen
        self.assets = assets
        self.new_game_b = Button(Position(
            (screensize[0] - assets["button"].get_size()[0]) // 2,
            (screensize[1] - assets["button"].get_size()[1]*4) // 5,    
        ), image=assets["button"].copy(), text="New Game",command=self.new_game, text_size=36)
        self.load_game_b = Button(Position(
            (screensize[0] - assets["button"].get_size()[0]) // 2,
            (screensize[1] - assets["button"].get_size()[1]*4) // 5 + assets["button"].get_size()[1] + (screensize[1] - assets["button"].get_size()[1]*4) // 5,    
        ), image=assets["button"].copy(), text="Load Game", text_size=36)
        self.options_b = Button(Position(
            (screensize[0] - assets["button"].get_size()[0]) // 2,
            (screensize[1] - assets["button"].get_size()[1]*4) // 5 + 2*(assets["button"].get_size()[1] + (screensize[1] - assets["button"].get_size()[1]*4) // 5),    
        ), image=assets["button"].copy(), text="Options", text_size=36)
        self.exit_b = Button(Position(
            (screensize[0] - assets["button"].get_size()[0]) // 2,
            (screensize[1] - assets["button"].get_size()[1]*4) // 5 + 3*(assets["button"].get_size()[1] + (screensize[1] - assets["button"].get_size()[1]*4) // 5),    
        ), image=assets["button"].copy(), text="Exit",command=self.exit, text_size=36)
        self.state = "main_menu"
    
    def on_event(self, event: Event):
        self.new_game_b.on_event(event)
        self.load_game_b.on_event(event)
        self.options_b.on_event(event)
        self.exit_b.on_event(event)
    
    def on_loop(self) -> str:
        self.new_game_b.on_loop()
        self.load_game_b.on_loop()
        self.options_b.on_loop()
        self.exit_b.on_loop()
        return(self.state)
    
    def on_render(self):
        self.screen.blit(self.new_game_b.render(), self.new_game_b.global_position.tuple())
        self.screen.blit(self.load_game_b.render(), self.load_game_b.global_position.tuple())
        self.screen.blit(self.options_b.render(), self.options_b.global_position.tuple())
        self.screen.blit(self.exit_b.render(), self.exit_b.global_position.tuple())
    
    def new_game(self):
        self.state = "village"
    
    def exit(self):
        self.state = "exit"