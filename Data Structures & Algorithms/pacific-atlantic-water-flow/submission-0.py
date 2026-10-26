from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        queue = deque()
        rows = len(heights)
        cols = len(heights[0])
        result = []
        for r in range(rows):

            queue.append((r,0,"Pacific"))
            queue.append((r,cols-1,"Atlantic"))
            pacific.add((r,0))
            atlantic.add((r,cols-1))
        
        for c in range(cols):
            queue.append((0,c,"Pacific"))
            queue.append((rows-1,c,"Atlantic"))

            pacific.add((0,c))
            atlantic.add((rows-1,c))
        
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        while queue:
            r,c,ocean = queue.popleft()

            for dr,dc in directions:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr>=rows or nc>=cols:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                
                if ocean == "Pacific" and (nr,nc) not in pacific:
                    pacific.add((nr,nc))
                    queue.append((nr,nc,"Pacific"))
                elif ocean == "Atlantic" and (nr,nc) not in atlantic:
                    atlantic.add((nr,nc))
                    queue.append((nr,nc,"Atlantic"))
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    result.append([r,c])
                
        return result
                



        
