class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i in range(len(nums)):
            
            if target - nums[i] in index.keys():
                return [index[target-nums[i]],i]
            else:
                index[nums[i]] = index.get(nums[i],0) + i
