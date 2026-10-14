class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]
        prod = 1
        i = 0
        while(i+1 < len(nums)):
            prod*=nums[i]
            prefix[i+1] = prod
            i+=1
        j = len(nums) - 1
        prod = 1
        while(j >= 1):
            prod*=nums[j]
            suffix[j-1] = prod
            j-=1
        
        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])

        return result