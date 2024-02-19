from typing import Self

class Node():
    def __init__(self, text:str, level:int) -> None:
        self.text = text
        self.level = level
        self.relatives = {}
        
    def add_connection(self, reaction :str, node :Self) -> None:
        self.relatives[reaction] = node