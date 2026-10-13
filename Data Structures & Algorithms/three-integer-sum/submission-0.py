class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 1. Sort is crucial
        ans = []
        
        for i in range(len(nums)):
            # 2. Outer Duplicate Check:
            # If this is the same number as the previous one, we've already 
            # solved for it. Skip it to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1 # Too big? Make it smaller
                elif total < 0:
                    left += 1  # Too small? Make it bigger
                else:
                    # Found a triplet!
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # 3. Inner Duplicate Check (The tricky part):
                    # We found a match, but now we need to move the pointers.
                    # We must SKIP any duplicate values to avoid printing 
                    # the exact same triplet again.
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return ans