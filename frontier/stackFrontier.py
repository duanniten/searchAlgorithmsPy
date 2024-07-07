from node import Node


class StackFrontier():
    def __init__(self) -> None:
        self.frontier = []
    
    def add(self, node: Node) -> None:
        self.frontier.append(node)
    
    def empty(self) -> bool:
        return len(self.frontier) == 0
    
    def containState(self, state: object) -> bool:
        return any(node.state == state for node in self.frontier)
    
    def remove(self) ->  Node:
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
