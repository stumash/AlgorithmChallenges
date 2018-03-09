def islandPerimeter(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    for (_row,_col) in [(row-1,col),(row,col-1),(row+1,col),(row,col+1)]:
                        if _row >= 0 and _row < len(grid) and _col >= 0 and _col < len(grid[0]):
                            if grid[_row][_col] == 0:
                                perimeter = perimeter + 1
                        else:
                            perimeter = perimeter + 1
        return perimeter

theGrid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(islandPerimeter(theGrid))
