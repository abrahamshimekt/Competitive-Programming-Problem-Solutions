class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 1
        while i < n-1:
            if (nums[i-1] + nums[i + 1])%2 == 0 and nums[i] == (nums[i-1] + nums[i + 1])//2 :
                nums[i] , nums[i + 1] = nums[i + 1], nums[i]
                if i > 1:
                    i -=1
            else:
                i +=1
        return nums