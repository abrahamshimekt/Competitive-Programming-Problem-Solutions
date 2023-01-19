class Solution:
    def find_smaller(self,nums,length,num):

        smaller_count = 0
        for index in range(length):
            if nums[index] < num:
                smaller_count +=1
                
        return smaller_count

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        length = len(nums)
        smallers_count = []

        for index in range(length):
            smaller_count = self.find_smaller(nums,length,nums[index])
            smallers_count.append(smaller_count)

        return smallers_count
