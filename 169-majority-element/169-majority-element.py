class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_nums = {}
        for num in nums:
            if num not in dict_nums:
                dict_nums[num] =1
            else:
                dict_nums[num] +=1
        for key in dict_nums:
            if dict_nums[key]> len(nums)//2:
                return key