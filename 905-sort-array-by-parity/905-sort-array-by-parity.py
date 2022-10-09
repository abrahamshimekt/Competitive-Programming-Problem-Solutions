class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 ==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for num in odd:
            even.append(num)
        return even
        