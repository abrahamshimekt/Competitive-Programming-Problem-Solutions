#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newNums = [0]*n
        for i in range(n):
            for j in range(n):
                if nums[i] > nums[j]:
                    newNums[i] += 1
        return newNums