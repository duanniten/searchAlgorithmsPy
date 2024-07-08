from node import Node
from frontier import StackFrontier
from maze import Maze

class bfs():
    def __init__(self, maze:Maze) -> None:
        self.num_explored = 0
        self.explored = set()
        self.maze = maze
        self.start = maze.start
        self.goal = maze.goal 

        self.frontier = StackFrontier()
        self.addNode(self.start)

      
    def solver(self):
        while True:
           
            if self.frontier.empty():
                raise Exception('no solution')
            
            node = self.frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(node.state)

            if len(node.neighboards) == 0:
                raise Exception ('no neigboards')

            for neighboard in node.neighboards:
                if (
                    not self.frontier.containState(neighboard) and
                    neighboard not in self.explored
                    ):
                    self.frontier.add(neighboard)
    
    def addNode(self, state):
        neighboards = self.maze.getNeighboards(state = state)
        self.frontier.add(
            Node(
                state = state,
                neighboards = neighboards
            )
        )
