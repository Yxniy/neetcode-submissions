import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [(x**2 + y**2,x,y) for x,y in points]
        heapq.heapify(heap)
        result = []

        while k:
            distance, x, y = heapq.heappop(heap)
            result.append([x,y])
            k-=1
        
        return result


            