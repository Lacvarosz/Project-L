from io import TextIOWrapper
from scripts.utils.stack import Stack
from scripts.model.text_graph import *
from typing import Any
from scripts.ml.utils import *

class Interact_reader():
    def __init__(self) -> None:
        self.lines = 0
    
    def readline(self, file :TextIOWrapper) -> str:
        while True:
            self.lines += 1
            ret = file.readline()
            ret = ret.split('#')[0].strip()
            if ret == "[interaction]":
                continue
            if ret == "[/interaction]":
                return("EOF")
            if ret:
                return(ret)
    
    def get_params(self, file :TextIOWrapper) -> tuple:
        params = {
            "text" : "Hello!",
            "id" : "",
            "repetable" : "yes",
            "level" : 0,
            "increment_level" : "no"
        }
        line = self.readline(file).split("=")
        while line[0][0] != '[':
            if len(line) == 1:
                raise IllegalFileFormat(f"Bed parameter definition in line {self.lines}!\n")
            params[line[0].strip()] = line[1].strip()
            line = self.readline(file).split("=")
        return((params, line[0]))
    
    def is_exist(self, k: Any, d :dict) -> Any:
        if k in ("repetable", "increment_level"):
            if d[k] == "yes":
                return(True)
            return(False)
        if k == "level":
            return(int(d[k]))
        return(d[k])
    
    def extra_connection(self, parent :Node, params:dict, inter :Interaction) -> None:
        if "connect" in params:
            for c in params["connect"].split(","):
                if c == "":
                    continue
                node = inter.search_id(c.strip())
                parent.add_connection(node)       
    
    def read(self, file :TextIOWrapper, lines :int = 0) -> tuple[Interaction, TextIOWrapper]:
        self.lines = lines
        struct = Stack[str]()
        nodes = Stack[Node]()
        line = self.readline(file)
        inter = None
        whithout_child = []
        while line:
            if line == "[act]":
                params, line = self.get_params(file)
                if struct.is_empty():
                    nodes.push(Node(params["text"],NodeType.ACTION,self.is_exist("level", params),self.is_exist("id", params), self.is_exist("repetable", params), self.is_exist("increment_level", params)))
                    self.extra_connection(nodes.peek(),params,inter)
                    if whithout_child == []:
                        inter = Interaction(nodes.peek())
                    else:
                        for n in whithout_child:
                            n.add_connection(nodes.peek())
                        whithout_child = []
                else:
                    c = nodes.peek()
                    nodes.push(Node(params["text"],NodeType.ACTION,self.is_exist("level", params),self.is_exist("id", params), self.is_exist("repetable", params), self.is_exist("increment_level", params)))
                    self.extra_connection(nodes.peek(),params,inter)
                    c.add_connection(nodes.peek())
                struct.push("[act]")
                
            elif line == "[react]":
                params, line = self.get_params(file)
                c = nodes.peek()
                nodes.push(Node(params["text"],NodeType.REACTION,self.is_exist("level", params),self.is_exist("id", params), self.is_exist("repetable", params), self.is_exist("increment_level", params)))
                self.extra_connection(nodes.peek(),params,inter)
                struct.push("[react]")
                c.add_connection(nodes.peek())
                
            elif line.startswith("[/"):
                if struct.peek() == "[" + line[2:]:
                    struct.pop()
                    node = nodes.pop()
                    if len(node.relatives) == 0:
                        whithout_child.append(node)
                else:
                    raise IllegalFileFormat(f"Some unclosed tag in line {self.lines}!")
                line = self.readline(file).split('#')[0].strip()
                
            elif line == "EOF":
                return(inter, file)
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