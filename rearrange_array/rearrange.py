class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        only_positive = []
        only_negative = []

        # separate the positives and the negatives

        for num in nums:

            if num > 0:
                only_positive.append(num)
            else:
                only_negative.append(num)

        rearranged_array = []

        for index in range(len(nums)//2):

            # always first append the positive to make positive - negative pattern in the array
            rearranged_array.append(only_positive[index])
            rearranged_array.append(only_negative[index])

        return rearranged_array


        
