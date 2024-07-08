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
            self.nodes = []


    def getNeighboards(self, state):
        (row, col) = state
        candidates = [
            ("up",      (row - 1, col   )),
            ("down",    (row + 1, col   )),
            ("left",    (row    , col-1 )),
            ("right",   (row    , col+1 ))
        ]
        neighboards = []
        for action, (r,c) in candidates:
            if (
                0 <= r < self.height and
                0 <= c <self.width and
                not self.walls[r][c]
                ):
                neighboards.append(action, (r,c))
        return neighboards

    def makeNode(self, state):
        action, neighboards = self.getNeighboards(state)
        node = Node(
            state = state,
            paren = None,
            action = None,
            neighboards = neighboards
        )
        self.nodes.append()