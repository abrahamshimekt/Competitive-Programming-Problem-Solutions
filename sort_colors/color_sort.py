class Solution:
    def find_min(self,nums,length,start):

        min_color = nums[start]
        pos = start

        for index in range(start+1,length):

            if nums[index] < min_color:
                min_color = nums[index]
                pos = index

        return min_color,pos

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for index in range(length):

            min_num,pos = self.find_min(nums,length,index)
            nums[index],nums[pos] = nums[pos],nums[index]
        