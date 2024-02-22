from typing import Self
from enum import Enum
from scripts.utils.stack import Stack

class NodeType(Enum):
    ACTION = 0
    REACTION = 1

class Node():
    def __init__(self, text:str, type :NodeType, level:int = 0, ide :str = "", repetable :bool = False) -> None:
        self.type = type
        self.text = text
        self.level = level
        self.id = ide
        self.repetable = repetable
        self.unread = True
        self.relatives = Stack[Node]()
        
    def add_connection(self, node :Self) -> None:
        self.relatives.push(node)
        
    def __str__(self):
        return(self.text)
    
    def read(self) -> str:
        self.unread = False
        print(self)
        return(str(self))

class Interaction():
    def __init__(self, start :Node):
        self.start_node = start
        self.remain = Stack[Node]()
        self.level = 1
    
    def search_id(self, ide :str)-> Node:
        def search(node :Node, ide :str)->Node:
            if node.id == ide:
                return(node)
            if node.relatives == []:
                return(None)
            for n in node.relatives:
                ret = search(n, ide)
                if ret is not None:
                    return(ret)
            return(None)
        return(search(self.start_node,ide))
    
    def start(self):
        self.remain.clear()
        self.remain.push(self.start_node)
    
    def next(self) -> bool:
        if len(self.remain):
            node = self.remain.pop()
            print(node)
            answeres = []
            for re in node.relatives.dat:
                if (re.repetable or re.unread) and re.level < self.level:
                    answeres.append(re)
                    print(len(answeres), end='. ')
                    re.read()
            if answeres != []:
                i = int(input("Válaszolj egy szám segítségével! "))
                answ = answeres[i-1]
                for i in answ.relatives:
                    if (i.repetable or i.unread) and i.level < self.level:
                        self.remain.push(i)
                return(True)
            return(False)