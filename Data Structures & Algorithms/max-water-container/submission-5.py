class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0
        left = 0
        right = len(heights) - 1
        most = 0
        while left < right:
            curr = min(heights[left],heights[right])*(right-left)

            most = max(curr,most)

            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
            
        
        return most

