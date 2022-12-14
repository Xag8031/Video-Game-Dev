import random

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

grid1 = [20, 20]
matrix = []
for i in range(grid1[0]):
    matrix.append([])
    for j in range(grid1[1]):
        matrix[i].append(random.randint(0, 10))
print(matrix)
grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(19, 19)
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)
print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
pause = input("Press the <ENTER> key to continue...")
