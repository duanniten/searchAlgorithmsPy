from node import Node

class Maze:
    def __init__(self, filename) -> None:
        with open(filename) as f:
            contents = f.read()
        
        if contents.count("S") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("G") != 1:
            raise Exception("maze must have exactly one goal")
        
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []

        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    state = contents[i][j]
                    if state == "S":
                        self.start = (i,j)
                        row.append(False)
                    elif state == "G":
                        self.goal = (i,j)
                        row.append(False)
                    elif state == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)


    def getNeighboards(self, node : Node) -> object:
        return node.action, node.state
