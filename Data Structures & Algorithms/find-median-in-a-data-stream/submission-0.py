import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max-heap using negatives
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:

        # Add to the appropriate heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # Rebalance the heaps
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(
                self.large,
                -heapq.heappop(self.small)
            )

        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(
                self.small,
                -heapq.heappop(self.large)
            )

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2