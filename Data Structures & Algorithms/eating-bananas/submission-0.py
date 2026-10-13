class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        big = max(piles)
        small = 1
        while small<=big:
            mid = (big + small) // 2
            hours = 0
            for n in range(len(piles)):

                curr = piles[n]

                hours += math.ceil(curr/mid)


            if hours > h:
                small = mid +1
            elif hours <= h:
                big = mid - 1
                
            
        return small

