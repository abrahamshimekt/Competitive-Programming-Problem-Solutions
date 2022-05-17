class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        not_in_nums = []
        for num in nums:
            dic[num] = 1
        for i in range(1,len(nums) +1):
            if i not in dic:
                not_in_nums.append(i)
        return not_in_nums
                
        