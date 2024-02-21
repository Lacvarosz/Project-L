from typing import TypeVar, Generic

T = TypeVar("T")
class Stack(Generic[T]):
    def __init__(self) -> None:
        self.dat = []
    
    def push(self, element :T) -> None:
        self.dat.append(element)
    
    def is_empty(self) -> bool:
        return(self.dat == [])
    
    def __len__(self) -> int:
        return(len(self.dat))
    
    def peek(self) -> T:
        return(self.dat[-1])
    
    def pop(self) -> T:
        ret = self.dat[-1]
        del self.dat[-1]
        return(ret)
    
    def clear(self) -> None:
        self.dat = []
        
    def __iter__(self):
        self.i = 0
        return(self)
    
    def __next__(self):
        self.i -= 1
        if -self.i <= len(self.dat):
            return(self.dat[self.i])
        else:
            raise StopIteration
    