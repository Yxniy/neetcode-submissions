class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in visited
            ):
                return False

            visited.add((r, c))

            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            visited.remove((r, c))
            return found

        # Try every cell as a possible starting point
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
                pass

        return False