class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        queue = collections.deque()
        for r in range(rows):
            if board[r][0] == 'O':
                queue.append((r,0))
                visited.add((r,0))
            if board[r][cols-1] == 'O':
                queue.append((r,cols-1))
                visited.add((r,cols-1))
        for c in range(cols):
            if board[0][c] == 'O':
                queue.append((0,c))
                visited.add((0,c))
            if board[rows-1][c] == 'O':
                queue.append((rows-1,c))
                visited.add((rows-1,c))

        directions = ((0,1),(0,-1),(1,0),(-1,0))

        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or board[nr][nc] != 'O':
                    continue
                
                visited.add((nr,nc))
                queue.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'

        
