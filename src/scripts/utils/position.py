from typing import *
from math import sqrt

class Position():
    def __init__(self, x :int = 0, y :int = 0) -> None:
        self.x = x
        self.y = y
    
    def set(self, x :int, y :int) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self, pos :Self) -> bool:
        return(pos.x == self.x and pos.y == self.y)
    
    def __add__(self, pos :Self) -> Self:
        return(Position(self.x + pos.x, self.y + pos.y))
    
    def __sub__(self, pos :Self) -> Self:
        return(Position(self.x - pos.x, self.y - pos.y))
    
    @overload
    def __mul__(self, pos :Self) -> int:
        return(self.x * pos.x + self.y * pos.y)
    
    def __mul__(self, n :int) -> Self:
        return(Position(self.x*n, self.y*n))
    
    def distance(pos1 :Self, pos2 :Self) -> float:
        return(sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2))
    
    def zero(self):
        self.x = self.y = 0
    
    def tuple(self) -> tuple[int, int]:
        return((self.x, self.y))
    
    def to_int(self) -> None:
        self.x = int(self.x)
        self.y = int(self.y)
    
    def __str__(self) -> str:
        return(f'({self.x}, {self.y})')
        