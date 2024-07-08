from node import Node

class Maze:
    def __init__(self) -> None:
        pass

    def getNeighboards(self, node : Node) -> object:
        return node.action, node.state
