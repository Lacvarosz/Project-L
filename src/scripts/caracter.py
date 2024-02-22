from scripts.text_graph import Interaction, Node
from scripts.utils.position import Position

class Caracter():
    def __init__(self, pos :Position = Position(), name:str="NJK") -> None:
        self.name = name
        self.pos = pos
        self.picture = "src/saki-monkeys-043.jpg"
    
    def move_up(self, y:int) -> None:
        self.pos.y -= y
    def move_down(self, y:int) -> None:
        self.pos.y += y
    def move_left(self, x:int) -> None:
        self.pos.x -= x
    def move_right(self, x:int) -> None:
        self.pos.x += x
        

class Player(Caracter):
    def __init__(self, pos: Position = Position(), name: str = "NJK") -> None:
        super().__init__(pos, name)