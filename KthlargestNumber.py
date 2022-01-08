class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [-int(i) for i in nums]
        heapq.heapify(maxHeap)
        while k > 1:
            heapq.heappop(maxHeap)
            k -=1
        return str(-maxHeap[0])