class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        subset = []

        def backtracking(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: Take nums[i]
            subset.append(nums[i])
            backtracking(i + 1)

            # Undo
            subset.pop()

            # Choice 2: Skip nums[i] and its duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtracking(i + 1)

        backtracking(0)
        return res