from io import TextIOWrapper
from scripts.utils.stack import Stack
from scripts.model.action import Action
from scripts.model.text_graph import Interaction
from typing import Any
from scripts.ml.utils import *

class Action_reader():
    def __init__(self, interaction :Interaction) -> None:
        self.lines = 0
        self.interaction = interaction
    
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
            "apply_to" : None,
            "increment" : None,
            "set" : None,
            "increase" : None
        }
        line = self.readline(file).split("=")
        while line[0] != 'EOF':
            if len(line) == 1:
                raise IllegalFileFormat(f"Bed parameter definition in line {self.lines}!\n")
            params[line[0].strip()] = line[1].strip()
            line = self.readline(file).split("=")
        return((params, line[0]))     
    
    def read(self, file :TextIOWrapper, lines:int = 0) -> tuple[Action, TextIOWrapper]:
        self.lines = lines
        struct = Stack[str]()
        action = None
        params, line = self.get_params(file)
        if params["apply_to"] is not None:
            if params["apply_to"] == "level":
                if params["increment"] == "yes":
                    action = Action(self.increment_level)
                elif params["set"] is not None:
                    self.value = int(params["set"])
                    action = Action(self.set_level)
                elif params["increase"] is not None:
                    self.value = int(params["increase"])
                    action = Action(self.increase_level)
            
        if line == "EOF":
            return(action, file)
        else:
            raise IllegalFileFormat(f"Something illegal in line {self.lines}!")
    
    def increment_level(self):
        self.interaction.level += 1
    
    def set_level(self):
        self.interaction.level = self.value
    
    def increase_level(self):
        self.interaction.level += self.value
        
                
if __name__ == "__main__":
    reader = Action_reader(open("src/test/interaction text format.txt","r",encoding="utf-8"))
    int, file = reader.read()
    int.start()
    while int.next(int(input("Válaszolj egy szám segítségével! "))-1):
        pass
    print("-------------------------", "\tAlles OK", "-------------------------", sep="\n")
    file.close()