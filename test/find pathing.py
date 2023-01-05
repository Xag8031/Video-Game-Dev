from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
def get_movement_directions(path):
    directions = []
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        if x1 < x2:
            directions.append("right")
        elif x1 > x2:
            directions.append("left")
        elif y1 < y2:
            directions.append("down")
        elif y1 > y2:
            directions.append("up")
    return directions
def get_path(matrix :list[list[int]], start_coords :list, end_coords :list):
    matrix = []
    xqvsb = 0
    for i in mat:
        matrix.append([])
        for j in i:
            if j ==1:
                matrix[xqvsb].append(0)
            elif j == 0:
                matrix[xqvsb].append(1)
        xqvsb += 1
    grid = Grid(matrix=matrix)

    start = grid.node(start_coords[0], start_coords[1])
    end = grid.node(end_coords[0], end_coords[1])

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    print(path) 
    return path
mat = [
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
points = [
    [0, 0],
    [13, 13],
    [8, 18],
    [11, 13],
    [16, 14],
    [16, 2],
    [2, 15],
    [8, 13],
    [4, 18],
    [12, 6],
    [16, 7],
    [16, 4],
    [18, 8],
    [14, 9],
    [3, 3],
    [5, 5],
    [18, 4],
    [13, 4],
    [16, 9],
    [2, 9],
    [18, 15],
    [9, 13],
    [17, 3],
    [17, 11],
    [15, 5],
    [2, 1],
    [17, 13],
    [15, 7],
    [12, 17],
    [10, 11],
    [16, 11]]
q = []

for i in range(len(points)-1):
    path = get_path(mat, points[i], points[i+1])
    directions = get_movement_directions(path)
    for direction in directions:
        q.append(direction)

print(q)
with open('code.creeps', 'w') as f:
    # Write the points list to the file, one point per line
    for dir in q:
        f.write(str(dir) + '\n')
print(f)