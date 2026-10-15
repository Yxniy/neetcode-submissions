class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxleft = 0
        maxright = 0
        left = 0
        right = len(height) - 1
        water = 0
        while left<=right:

            maxleft = max(height[left],maxleft)
            maxright = max(height[right],maxright)

            if maxleft <= maxright:
                water+= min(maxleft,maxright) - height[left] if min(maxleft,maxright) - height[left] > 0 else 0

                left+=1
            else:
                water+= min(maxleft,maxright) - height[right] if min(maxleft,maxright) - height[right] > 0 else 0
                right-=1
        
        return water



