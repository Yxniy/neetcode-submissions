class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        dp = [nums[0],max(nums[0],nums[1])]

        for n in range(2,len(nums)):
            dp.append(max(nums[n]+dp[n-2],dp[n-1]))

        return dp[-1]