class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        left_product = [1]

        for left in range(size):
            left_product.append(nums[left]*left_product[left])

        right_product = [nums[size-1]]

        for right in range(size-2,-1,-1):
            right_product.append(nums[right]*right_product[size-right-2])

        right_product = right_product[::-1]
        right_product.append(1)

        product_excepts = []
        for index in range(len(nums)):
            product_excepts.append(left_product[index]*right_product[index+1])

        return product_excepts

        