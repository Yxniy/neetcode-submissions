class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmin = float('inf')
        maxprofit = 0
        profit = 0
        left = 0
        right = 0

        while right <= len(prices) - 1:
            maxprofit = max(maxprofit, prices[right] - prices[left])

            if prices[right] <= prices[left]:
                left = right
            
            right+=1

            

            

        return maxprofit