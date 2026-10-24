class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtracking():
            
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            
            for i in nums:
                if i in subset:
                    continue
                
                subset.append(i)
                
                backtracking()
                subset.pop()

        backtracking()
        return res