class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums + [float('-inf')]
        heapify(self.min_heap)
        while len(self.min_heap) > k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappushpop(self.min_heap, val)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)