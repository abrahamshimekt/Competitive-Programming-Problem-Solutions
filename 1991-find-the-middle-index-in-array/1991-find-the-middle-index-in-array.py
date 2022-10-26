class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == 0:
                if sum(nums[1:])==0:
                     return 0
                i +=1
            elif i== len(nums)-1 :
                if sum(nums[:i]) ==0:
                    return i
                i +=1
            elif sum(nums[i+1:]) == sum(nums[:i]):
                return i
            else:
                i +=1
        return -1