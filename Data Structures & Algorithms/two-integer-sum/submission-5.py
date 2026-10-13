class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for n in range(len(nums)):
            numdict[nums[n]] = n

        for n in range(len(nums)):
            x = target - nums[n]
            if x in numdict.keys():
                if numdict[x] != n:
                    return[n,numdict[x]] 

        return -1
