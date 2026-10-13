class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol, ans = [],[]
        def backtracking(i):
            if i == n:
                ans.append(sol[:])
                return 
            
            backtracking(i+1)
            
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

        backtracking(0)

        return ans
