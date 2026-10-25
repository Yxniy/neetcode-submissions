class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        subset = []

        def backtrack(openCount, closeCount):

            # What condition means we have a complete string?
            if openCount==closeCount==n:
                result.append("".join(subset))
                return

            if openCount < n:
                subset.append("(")
                backtrack(openCount + 1, closeCount)
                subset.pop()

            if closeCount < openCount:
                subset.append(")")
                backtrack(openCount, closeCount + 1)
                subset.pop()

        backtrack(0, 0)
        return result