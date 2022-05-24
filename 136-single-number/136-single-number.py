class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic_nums = {}
        for num in nums:
            if num not in dic_nums:
                dic_nums[num] = 1
            else:
                dic_nums[num] +=1
        for key in dic_nums:
            if dic_nums[key] == 1:
                return key
        