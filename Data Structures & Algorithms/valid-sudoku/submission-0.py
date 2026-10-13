class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        grid = [[set() for _ in range(3)] for _ in range(3)]
        
        for c in range(len(board)):
            for r in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in grid[r // 3][c//3]:
                    return False
            
                col[c].add(board[r][c]) 
                row[r].add(board[r][c])
                grid[r//3][c//3].add(board[r][c]) 


        return True