class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for i in range(len(nums)):
            if nums[i] not in nums_index:
                nums_index[nums[i]] = i
        print(nums_index)
        for i in range(len(nums)):
            if target-nums[i] in nums_index and i !=nums_index[target-nums[i]] :
                return [i,nums_index[target-nums[i]]]