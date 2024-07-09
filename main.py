from maze import Maze
from solvers import BFS
from utilits import outputImage

maze1 = Maze('mazes_test\maze1.txt')
bfs = BFS(maze= maze1)
bfs.solver()

outputImage(
    Savefilename="images\maze1_bfs.png",
    solver= bfs,
    maze= maze1,
    show_explored= True
)
