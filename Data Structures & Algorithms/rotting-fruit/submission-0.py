from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        freshfruit = 0
        maxtime = 0
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    freshfruit+=1
                
        
        while queue:
            r,c,time = queue.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                freshfruit-=1
                maxtime = max(maxtime,time+1)
                queue.append((nr,nc,time+1))
        
        return maxtime if freshfruit == 0 else -1
        


                

