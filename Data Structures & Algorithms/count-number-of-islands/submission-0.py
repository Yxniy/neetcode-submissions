class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, x, y):
            if grid[x][y] == '1':
                grid[x][y] = '0'
                if 0 < x:
                    bfs(grid,x-1,y)
                if x < len(grid) -1:
                    bfs(grid,x+1,y)
                if 0 < y:
                    bfs(grid, x,y-1)
                if y < len(grid[0])-1:
                    bfs(grid, x,y+1)
        islands = 0
        row = len(grid)
        col = len(grid[0])
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    islands+=1
                    bfs(grid,x,y)             
        return islands  
            
            