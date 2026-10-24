class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                # Save the completed subset
                result.append(subset.copy())
                return

            # Choice 1: Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Undo that choice
            subset.pop()

            # Choice 2: Exclude nums[i]
            backtrack(i + 1)

        backtrack(0)

        return result