class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j]>nums[j + 1]:
                    nums[j],nums[j +1] = nums[j +1],nums[j]
        index =[]
        for k in range(n):
            if nums[k] == target:
                index.append(k)
        return index
