from maze import Maze
from solvers import BFS

maze1 = Maze('mazes_test\maze1.txt')
bfs = BFS(maze= maze1)
bfs.solver()
print(bfs.solution)