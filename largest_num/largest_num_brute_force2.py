class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        length = len(nums)

        for index in range(length):
            nums[index] = str(nums[index])

        for index_i in range(length):

            for index_j in range(index_i+1,length):

                if int(nums[index_i] + nums[index_j]) < int(nums[index_j]+ nums[index_i]):
                    nums[index_i],nums[index_j] = nums[index_j],nums[index_i]

        return "0" if nums[0] == '0' else ''.join(nums)