from maze import Maze
from solvers import BFS, DPS
from utilits import outputImage

maze1 = Maze('mazes_test\maze2.txt')
bfs = DPS(maze= maze1)
bfs.solver()

outputImage(
    Savefilename="images\maze2_dps.png",
    solver= bfs,
    maze= maze1,
    show_explored= True,
)
