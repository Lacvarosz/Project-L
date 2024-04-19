from io import TextIOWrapper
from scripts.utils.stack import Stack
from scripts.model.text_graph import *
from typing import Any
from scripts.ml.utils import *

class Action_reader():
    def __init__(self) -> None:
        self.lines = 0
    
    def readline(self, file :TextIOWrapper) -> str:
        while True:
            self.lines += 1
            ret = file.readline()
            ret = ret.split('#')[0].strip()
            if ret == "[action]":
                continue
            if ret == "[/action]":
                return("EOF")
            if ret:
                return(ret)
    
    def get_params(self, file :TextIOWrapper) -> tuple:
        params = {
            "set_level" : -1,
            "change_level_by" : 0,
        }
        line = self.readline(file).split("=")
        while line[0][0] != '[':
            if len(line) == 1:
                raise IllegalFileFormat(f"Bed parameter definition in line {self.lines}!\n")
            params[line[0].strip()] = line[1].strip()
            line = self.readline(file).split("=")
        return((params, line[0]))     
    
    def read(self, file :TextIOWrapper, lines:int = 0) -> tuple[Interaction, TextIOWrapper]:
        self.lines = lines
        struct = Stack[str]()
        nodes = Stack[Node]()
        line = self.readline(file)
        inter = None
            
        if line == "EOF":
            return(inter, file)
        else:
            raise IllegalFileFormat(f"Something illegal in line {self.lines}!")
        
                
if __name__ == "__main__":
    reader = Action_reader(open("src/test/interaction text format.txt","r",encoding="utf-8"))
    int, file = reader.read()
    int.start()
    while int.next(int(input("Válaszolj egy szám segítségével! "))-1):
        pass
    print("-------------------------", "\tAlles OK", "-------------------------", sep="\n")
    file.close()