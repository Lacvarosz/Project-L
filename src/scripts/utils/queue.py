from typing import TypeVar, Generic

T = TypeVar("T")
class Queue(Generic[T]):
    def __init__(self) -> None:
        self.dat = []
    
    def push(self, element :T) -> None:
        self.dat.append(element)
    
    def is_empty(self) -> bool:
        return(self.dat == [])
    
    def __len__(self) -> int:
        return(len(self.dat))
    
    def top(self) -> T:
        return(self.dat[0])
    
    def pop(self) -> T:
        ret = self.dat[0]
        del self.dat[0]
        return(ret)
    
    def clear(self) -> None:
        self.dat = []
    