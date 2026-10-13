class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areas = [0]
        index = 0
        def bfs(grid, x, y,index,areas):

            if grid[x][y] == 1:
                areas[index] += 1
                grid[x][y] = 0
                if 0 < x:
                    bfs(grid,x-1,y,index,areas)
                if x < len(grid) -1:
                    bfs(grid,x+1,y,index,areas)
                if 0 < y:
                    bfs(grid, x,y-1,index,areas)
                if y < len(grid[0])-1:
                    bfs(grid, x,y+1,index,areas)
        
        row = len(grid)
        col = len(grid[0])
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    index+=1
                    areas.append(0)
                    bfs(grid,x,y,index,areas)   
        ans = max(areas) if areas else 0          
        return ans
            
            