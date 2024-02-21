from utils.position import Position
from caracter import Player
class Map():
    def __init__(self, pos: Position = Position(), player :Player = Player(), picture:str = "") -> None:
        self.pos = pos
        self.player = player
        self.picture = "src/Képkivágás.png"
    
    def set_pos(self, size:tuple[int,int]):
        self.pos = (Position(size[0]/2, size[1]/2) - self.player.pos)
        print(self.pos)