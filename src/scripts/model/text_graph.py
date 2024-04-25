from typing import Self
from enum import Enum
from scripts.model.action import Action
from scripts.utils.stack import Stack

class NodeType(Enum):
    ACTION = 0
    REACTION = 1

class Node():
    def __init__(self, text:str, type :NodeType, level:int = 0, ide :str = "", repetable :bool = False, action :Action = None) -> None:
        self.type = type
        self.text = text
        self.level = level
        self.id = ide
        self.repetable = repetable
        self.unread = True
        self.action = action
        self.relatives = Stack[Node]()
        
    def add_connection(self, node :Self) -> None:
        self.relatives.push(node)
        
    def __str__(self):
        return(self.text)
    
    def read(self) -> str:
        self.unread = False
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
        self.level = 1
    
    def get(self) -> list[str]:
        if not self.remain.is_empty():
            node = self.remain.peek()
            ret = [str(node)]
            for re in node.relatives.dat:
                    if (re.repetable or re.unread) and re.level < self.level:
                        ret.append(str(re))
            return(ret)
        return []
    
    def next(self, i :int) -> list[str]:
        if not self.remain.is_empty():
            node = self.remain.peek()
            answeres = []
            for re in node.relatives.dat:
                if (re.repetable or re.unread) and re.level < self.level:
                    answeres.append(re)
                    re.read()
            if len(answeres) > i:
                self.remain.pop()
                answ = answeres[i]
                if answ.action is not None:
                    answ.action.execute()
                for i in answ.relatives:
                    if (i.repetable or i.unread) and i.level < self.level:
                        self.remain.push(i)
            return not self.remain.is_empty()
        return False