class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        i ,j= 0,0
        q = deque()
        while j < len(nums):
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)
            if i > q[0]:
                q.popleft()
            if j + 1 >= k:
                output.append(nums[q[0]])
                i +=1
            j +=1
        return output