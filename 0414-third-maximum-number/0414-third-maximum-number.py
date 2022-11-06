class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        distinct = [nums[0]]
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != curr:
                curr = nums[i]
                distinct.append(nums[i])
        n = len(distinct)
        if n-3 >=0:
            return distinct[n-3]
        else:
            return max(distinct)