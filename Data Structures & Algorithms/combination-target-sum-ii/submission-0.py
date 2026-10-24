class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        subset = []

        def backtracking(i, total):
            if total == target:
                result.append(subset.copy())
                return

            if i == len(candidates) or total > target:
                return

            # Choice 1: Take the number
            subset.append(candidates[i])
            backtracking(i + 1, total + candidates[i])

            # Undo
            subset.pop()

            # Choice 2: Don't take the number
            # Skip all duplicates of the current number
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtracking(i + 1, total)

        backtracking(0, 0)
        return result