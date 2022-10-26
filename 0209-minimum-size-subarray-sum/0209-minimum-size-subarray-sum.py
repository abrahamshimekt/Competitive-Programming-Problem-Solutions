class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        i = j = 0
        count = float("inf")
        while i < len(nums):
            if running_sum < target and j <len(nums):
                running_sum += nums[j]
                j +=1
            elif running_sum>= target:
                count = min(count,j-i)
                running_sum -= nums[i]
                i +=1
            else:
                break
        return 0 if count == float("inf") else count