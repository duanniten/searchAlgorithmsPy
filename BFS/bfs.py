from node import Node
from frontier import StackFrontier
from maze import Maze

class bfs():
    def __init__(self, startNode : Node, goal: object) -> None:
        self.num_explored = 0
        self.explored = set()
        self.start = startNode
        self.frontier = StackFrontier()
        self.frontier.add(startNode.state)
        self.goal = goal
        self.maze = None

    def getMaze(self, maze : Maze):
        self.maze = maze
        
    def solver(self):
        while True:

            if self.maze == None:
                raise Exception('There is no maze')
            
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

            for action, state in self.maze.getNeighboard(node):
                if not self.frontier.containState(state) and state not in self.explored:
                    child = Node(state= state, parent= node, action= action)

