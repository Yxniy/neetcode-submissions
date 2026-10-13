class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxi = 0
        left = 0
        right = len(heights) -1
        

        while left < right:
            curr = (right - left) * min(heights[right],heights[left])
            maxi = max(maxi,curr)
            if heights[right] >= heights[left]:
                left+=1
            elif heights[right] <= heights[left]:
                right-=1
            
            else: 
                 break

        
        
        return maxi


            