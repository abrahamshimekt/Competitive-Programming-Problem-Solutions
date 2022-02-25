from ast import List
class Solution:
    @staticmethod
    def is_common_difference(nums):
        d = set()
        nums.sort()
        for i in range(1,len(nums)):
            d.add(nums[i]-nums[i-1])
            if len(d) > 1:
                return False
        return True
        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [self.is_common_difference(nums[x:y + 1]) for x,y in zip(l,r)]