from io import TextIOWrapper
from scripts.model.text_graph import *
from scripts.ml.utils import *
from typing import Any
from scripts.utils.position import Position
from scripts.utils.animation import Animation

class Animation_reader():
    def __init__(self, assets, tile_size) -> None:
        self.lines = 0
        self.assets = assets
        self.tile_size = tile_size
    
    def readline(self, file :TextIOWrapper) -> str:
        while True:
            self.lines += 1
            ret = file.readline()
            ret = ret.split('#')[0].strip()
            if ret == "[animation]":
                continue
            if ret == "[/animation]":
                return("EOF")
            if ret:
                return(ret)
    
    def get_params(self, file :TextIOWrapper) -> tuple:
        params = {
            "position" : "0, 0",
            "has_collision" : "no",
            "collision" : "0, 0, 0, 0",
            "name" : "Hello!",
            "speed" : "1",
            "size" : "0,0",
            "interaction" : None,
            "animation" : self.assets["village_elder"].copy()
        }
        line = self.readline(file).split("=")
        print(line)
        while line[0] != 'EOF':
            
            if line[0] == "[interaction]":
                params["interaction"], file = Interact_reader().read(file, self.lines)
            elif line[0] == "[animation]":
                params["animation"], file = Animation_reader().read(file, self.lines)
            elif len(line) == 1:
                raise IllegalFileFormat(f"Bed parameter definition in line {self.lines}!\n")
            else:
                params[line[0].strip()] = line[1].strip()
            line = self.readline(file).split("=")
            print(line)
        return((params, line[0]))
    
    def is_exist(self, k: Any, d :dict) -> Any:
        if k == "has_collision":
            if d[k] == "yes":
                return(True)
            return(False)
        if k == "speed":
            return(float(d[k]))
        if k == "position":
            tmp = [int(i) for i in d[k].strip().split(",")]
            d[k] = Position(tmp[0], tmp[1]) * self.tile_size
        if k in ("collision", "size"):
            d[k] = tuple([int(i) for i in d[k].strip().split(",")])
        return(d[k])   
    
    def read(self, file :TextIOWrapper, lines :int = 0) -> tuple[Interaction, TextIOWrapper]:
        self.lines = lines
        npc = None
        params, line = self.get_params(file)
        
        npc = Npc(params["interaction"], params["animation"], self.is_exist("position", params),self.is_exist("has_collision", params),params["name"],self.is_exist("speed", params),self.is_exist("size", params),self.is_exist("collision", params))
        
        if line == "EOF":
            return(npc, file)
        else:
            raise IllegalFileFormat(f"Something illegal in line {self.lines}!")
        
                
if __name__ == "__main__":
    reader = Interact_reader(open("src/test/interaction text format.txt","r",encoding="utf-8"))
    int, file = reader.read()
    int.start()
    while int.next(int(input("Válaszolj egy szám segítségével! "))-1):
        pass
    print("-------------------------", "\tAlles OK", "-------------------------", sep="\n")
    file.close()