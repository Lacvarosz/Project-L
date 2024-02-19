from utils.text_graph import Node
from utils.position import Position
class Caracter():
    def __init__(self, text:Node, pos :Position, name:str="NJK") -> None:
        self.name = name
        self.pos = pos
        if text is None:
            self.text = Node(f"Hi, I'm {name}.\nNice to meet you.")
        else:
            self.text = text
        
    
    