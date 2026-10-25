class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areas = [0]
        rows = len(grid)
        cols = len(grid[0])
        i=0
        def dfs(r,c,i):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            areas[i] += 1
            dfs(r+1,c,i)
            dfs(r-1,c,i)    
            dfs(r,c-1,i)
            dfs(r,c+1,i)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    i+=1
                    areas.append(0)
                    dfs(r,c,i)

        return max(areas)