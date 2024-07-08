from node import Node
from frontier import StackFrontier

class bfs():
    def __init__(self, startNode : Node, goalNode : Node) -> None:
        self.num_explored = 0
        self.explored = set()
        self.start = startNode
        self.goal = goalNode
        self.frontier = StackFrontier()
        self.frontier.add(startNode.neighboards)

      
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

            for neighboar in node.neighboards:
                if (
                    not self.frontier.containState(neighboar.state) and
                    neighboar.state not in self.explored
                    ):
                    self.frontier.add(neighboar)
