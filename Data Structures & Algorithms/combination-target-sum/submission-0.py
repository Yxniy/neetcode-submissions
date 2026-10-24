class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i, total):

            # Base case 1: Found a valid combination
            if total == target:
                result.append(subset.copy())
                return

            # Base case 2: Cannot continue
            if total > target or i == len(nums):
                return

            # Choice 1: Take nums[i]
            subset.append(nums[i])
            backtrack(i, total + nums[i])

            # Undo
            subset.pop()

            # Choice 2: Skip nums[i]
            backtrack(i+1, total)

        backtrack(0, 0)
        return result