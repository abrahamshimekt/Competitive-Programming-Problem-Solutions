from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [0]*(n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        queue = deque()
        result = n + 1
        for i in range(n +1):
            while queue and prefix_sums[i] - prefix_sums[queue[0]] >= k:
                result = min(result, i - queue.popleft())
            while queue and prefix_sums[queue[-1]] >= prefix_sums[i]:
                queue.pop()
            queue.append(i)
        return result if result <=n else -1