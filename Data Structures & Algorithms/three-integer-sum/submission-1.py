class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result_set = []
        result = []
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if -nums[i] == nums[left] + nums[right] and set([nums[i],nums[left],nums[right]]) not in result_set:
                    result_set.append(set([nums[i],nums[left],nums[right]]))
                    result.append([nums[i],nums[left],nums[right]])
                elif -nums[i] > nums[left] + nums[right]:
                    left+=1
                else:
                    right-=1
            
        
        return result
                