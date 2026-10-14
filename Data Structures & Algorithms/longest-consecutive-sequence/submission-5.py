class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0
        

        for n in nums_set:
            if n-1 not in nums_set:
                curr = 1
                while (n+1 in nums_set):
                    curr+=1
                    n+=1
                
                longest = max(longest,curr)

        return longest


        