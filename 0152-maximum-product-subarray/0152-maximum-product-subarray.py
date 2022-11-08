class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        max_product =nums[0]
        min_product = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] <0:
                max_product,min_product = min_product,max_product
            max_product = max(max_product*nums[i],nums[i])
            min_product = min(min_product*nums[i],nums[i])
            ans = max(ans,max_product)
            i +=1
        return ans

        