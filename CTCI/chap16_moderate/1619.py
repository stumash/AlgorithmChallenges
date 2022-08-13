from typing import List

def pond_sizes(pond):
    ps = []
    n_rows, n_cols = len(pond), len(pond[0])
    visited = set()
    for i,row in enumerate(pond):
        for j,_ in enumerate(row):
            is_water = pond[i][j] == 0
            is_unvisited = (i,j) not in visited
            if is_water and is_unvisited:
                ps.append(pond_size(i, j, pond, n_rows, n_cols, visited))
    return ps

def pond_size(i, j, pond, n_rows, n_cols, visited) -> int:
    not_water = pond[i][j] != 0
    is_visited = (i,j) in visited
    if not_water or is_visited:
        return 0
    visited.add((i,j))
    neighbors = [(x,y) for x,y in [
        (i-1,j-1),
        (i-1,j),
        (i-1,j+1),
        (i,j-1),
        (i,j+1),
        (i+1,j-1),
        (i+1,j),
        (i+1,j+1),
    ] if x>=0 and x<n_rows and y>=0 and y<n_cols and pond[x][y] == 0]
    return 1 + sum(pond_size(x,y,pond,n_rows,n_cols,visited) for x,y in neighbors)

pond = [
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1],
]
print(pond_sizes(pond))
