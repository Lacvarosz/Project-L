from scripts.text_graph import Interaction, Node
from scripts.utils.position import Position

class Caracter():
    def __init__(self, pos :Position = Position(), name:str="NJK") -> None:
        self.name = name
        self.pos = pos
        self.picture = "src/saki-monkeys-043.jpg"
        

class Player(Caracter):
    def __init__(self, pos: Position = Position(), name: str = "NJK") -> None:
        super().__init__(pos, name)
    
    def move_up(self, y:int, map_size :tuple[int, int], player_size :tuple[int, int]) -> None:
        if self.pos.y - y > 0:
            self.pos.y -= y
    
    def move_down(self, y:int, map_size :tuple[int, int], player_size :tuple[int, int]) -> None:
        if self.pos.y + player_size[1] + y < map_size[1]:
            self.pos.y += y
    def move_left(self, x:int, map_size :tuple[int, int], player_size :tuple[int, int]) -> None:
        if self.pos.x - x > 0:
            self.pos.x -= x
    def move_right(self, x:int, map_size :tuple[int, int], player_size :tuple[int, int]) -> None:
        if self.pos.x + x +player_size[0] < map_size[0]:
            self.pos.x += x